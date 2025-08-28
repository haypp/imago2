from app import reformat_array
import json

test_data = [
    {"id": 1, "name": "Alice", "category": "A", "sub_category": "X"},
    {"id": 2, "name": "Bob", "category": "B", "sub_category": "Y"},
    {"id": 3, "name": "Charlie", "category": "A", "sub_category": "Z"},
    {"id": 4, "name": "David", "category": "B", "sub_category": "X"}
]

def test_function():
    """Test the reformat_array function directly"""
    result = reformat_array(test_data)
    print("Function Output:")
    print(json.dumps(result, indent=2))
    
    expected = {
        "A": {
            "X": [{"id": 1, "name": "Alice"}],
            "Z": [{"id": 3, "name": "Charlie"}]
        },
        "B": {
            "Y": [{"id": 2, "name": "Bob"}],
            "X": [{"id": 4, "name": "David"}]
        }
    }
    
    print("\nExpected Output:")
    print(json.dumps(expected, indent=2))
    
    if result == expected:
        print("\n✓ Test PASSED")
    else:
        print("\n✗ Test FAILED")
        print("Differences:")
        for category in expected:
            if category not in result:
                print(f"  Missing category: {category}")
                continue
            for subcat in expected[category]:
                if subcat not in result[category]:
                    print(f"  Missing subcategory: {category}.{subcat}")
                    continue
                if result[category][subcat] != expected[category][subcat]:
                    print(f"  Mismatch in {category}.{subcat}")
                    print(f"    Expected: {expected[category][subcat]}")
                    print(f"    Got:      {result[category][subcat]}")

if __name__ == "__main__":
    test_function()
