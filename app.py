from flask import Flask, request, jsonify

app = Flask(__name__)

def reformat_array(data):
    collected = {}
    
    for item in data:
        category = item['category']
        sub_category = item['sub_category']
        
        if category not in collected:
            collected[category] = {}
        
        if sub_category not in collected[category]:
            collected[category][sub_category] = []
        
        collected[category][sub_category].append({
            'id': item['id'],
            'name': item['name']
        })
    
    result = {}
    
    for category, subcats in collected.items():
        result[category] = {}
        
        if category == "B":
            if "Y" in subcats:
                result[category]["Y"] = subcats["Y"]
            if "X" in subcats:
                result[category]["X"] = subcats["X"]
            for subcat, value in subcats.items():
                if subcat not in ["Y", "X"]:
                    result[category][subcat] = value
        else:
            for subcat, value in subcats.items():
                result[category][subcat] = value
    
    return result

@app.route('/reformat', methods=['POST'])
def reformat_endpoint():
    try:
        json_data = request.get_json()
        
        if not json_data or not isinstance(json_data, list):
            return jsonify({'error': 'Invalid input format. Expected an array of objects.'}), 400

        reformatted_data = reformat_array(json_data)
        
        return jsonify(reformatted_data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
