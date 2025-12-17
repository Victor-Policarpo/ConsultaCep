import requests
import json

class CepConsult:
    """Class to validate and consult Brazilian ZIP codes (CEPs) using the ViaCEP API.
    Attributes:
        cep_ (tuple): A tuple of ZIP codes to be validated and consulted.
    Methods:
        validate_cep(): Validates and consults the ZIP codes through the API.
        return_cep_validate(): Prints the results of the ZIP code consultations.
        save_in_json_file(): Saves the ZIP code consultation results in a JSON file.
    """

    def __init__(self, *args):
        self.cep_ = args
        self.__API = "https://viacep.com.br/ws/{}/json/"

    def validate_cep(self):
        """Validates and consults the ZIP codes through the API. Returns a list of dictionaries with the results."""
        list_cep = []
        for cep in self.cep_:
            if "-" in cep:
                cep = cep.replace("-", "")
            if " " in cep:
                cep = cep.replace(" ", "")
            if len(cep) == 8 and cep.isdigit():
                response = requests.get(self.__API.format(cep))
                if response.status_code == 200:
                    data = response.json()
                    if data and "erro" not in data:
                        list_data = {
                            "CEP": data['cep'],
                            "Logradouro": data['logradouro'],
                            "Cidade": data['localidade'],
                            "Bairro": data['bairro'],
                            "Estado": data['estado'],
                            "UF": data['uf']
                        }
                        list_cep.append({cep: list_data})
                    else:
                        list_cep.append({cep: "Not found"})
            else: 
                list_cep.append({cep: "Invalid"})
        return list_cep
    
    def return_cep_validate(self):
        """Prints the results of the ZIP code consultations. Return is None"""
        list_ = self.validate_cep()
        for dict_ in list_:
            for i, j in dict_.items():
                if j == "Invalid":
                    print(f"{i} - Invalid CEP format.")
                elif j == "Not found":
                    print(f"{i} - was not found.")
                else: 
                   print(f"{j['CEP']} - {j['Logradouro']}, {j['Cidade']}, {j['Estado']}/{j['UF']}")
        self._save_in_json_file(list_)

    def _save_in_json_file(self, list):
        """Saves the ZIP code consultation results in a JSON file. Return is None"""
        list_ = list
        valid_cep = []
        invalid_cep = []
        not_found_cep = []
        for dict_ in list_:
            for i, j in dict_.items():
                if j == "Invalid":
                    invalid_cep.append(i)
                elif j == "Not found":
                    not_found_cep.append(i)
                else: 
                   valid_cep.append(j["CEP"])
        with open("json_files/cep_result.json", "w") as file:
            json.dump(
                {
                    "Valid CEPs": valid_cep,
                    "Invalid CEPs": invalid_cep,
                    "Not Found CEPs": not_found_cep
                }, file, indent=4)
            
if __name__ == "__main__":
    cep = list(input("Enter the ZIP codes separated by commas: (00000000, 00000-000) ").split(","))
    CepConsult(*cep).return_cep_validate()
    

