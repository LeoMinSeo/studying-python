import os
import  requests
from flask_cors import  CORS
from flask import Flask,jsonify,request
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()


app = Flask(__name__)
CORS(app)

@app.route('/transdata',methods=['POST'])
def transdata():
    data = request.get_json()
    message = data

    url_for_deepl = 'https://api-free.deepl.com/v2/translate'
    params = {'auth_key':os.getenv('DEEPL_API_KEY'),'text':message ,'source_lang' : 'KO', "target_lang": 'EN'}
    result = requests.post(url_for_deepl, data=params, verify=False)
    print(result.json()['translations'][0]["text"])
    return jsonify({"result":result.json()['translations'][0]["text"]})

if __name__ == "__main__":
    app.run(debug=True)