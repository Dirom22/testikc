
import json
 
class Model:
    title = '1'
    text = '2'
    autor = '3'

    def save(self):
        dct = {k: str(v) for k, v in vars(Model).items()}
        with open('M5-2-1.json', 'w', encoding='utf-8') as fout:
            json.dump(dct, fout)
 
obj = Model()
obj.save()

