import re


def get_result(matches):
    """Gets match results from the user."""
    print("Please provide your predictions for following matches, use format 'X:Y', where X and Y are numbers!")
    predictions = []
    for match in matches:
        while True:
            result = input(f"{match} : ")
            if validate_result(result):
                predictions.append(result)
                break
            else:
                print("Incorrect predictions format. Use format 'X:Y', where X and Y are numbers!")
    return predictions


def validate_result(result):
    """Checks, if the match result is in the correct format."""
    return bool(re.match(r'^\d+:\d+$', result))


def compare_results(matches, match_result, predictions):
    """Compares the results of matches from the list match_result and predictions."""
    for i, match in enumerate(matches):
        result_m1 = match_result[i]
        result_m2 = predictions[i]

        if result_m1 == result_m2:
            print(f"Match result {match} is the same as your prediction: {result_m1}")
        else:
            print(f"Match result {match} is different: {result_m1} than your prediction: {result_m2}")


# Main code
if __name__ == "__main__":
    matches = ["BVB vs AFC", "Stuttgart vs Bayern"]
    match_result = ["5:1", "3:1"]
    typ = get_result(matches)
    compare_results(matches, match_result, typ)