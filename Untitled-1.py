
@app.route('/email',methods=['POST'])
def generateemai():
    if request.method=='POST':
        request_attr=request.get_json()
    else:
        request_attr=request.args
    video = request_attr.get('video',None)
    unique = request_attr.get('unique',None)
    note = request_attr.get('note',None)

    try:
        if not video:
            return jsonify({'error':'video id is missing'})

        if not unique:
            return jsonify({'error':'unique id is missing'})

        if not note:
            return jsonify({'error':'note is missing'})

        prompt = "This is the testing prompt"
        response = callopenai.openai_completions_scalar(input=note, prompt=prompt,inputtype="text", fileid=unique)
        if "error" in response:
            return jsonify({'error':'Error found in response'})
        else:
            data = "Generated Summary from OpenAI"
    except Exception as e:
        print(f"Error Occured {str(e)}")
    
    except Exception as e:
        print(f"Error Occured {str(e)}")