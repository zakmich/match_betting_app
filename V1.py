matches = ["BVB vs AFC", "Stuttgart vs Bayern"]
match_result = ["5:1", "3:1"]
prediction = []

for match in matches:
    result = input(f"Please insert your prediction for match, {match}: ")
    prediction.append(result)

for i, match in enumerate(matches):
    result_m1 = match_result[i]
    result_m2 = prediction[i]

    if result_m1 == result_m2:
        print(f"Match result {match} is the same as your prediction: {result_m1}")
    else:
        print(f"Match result {match} is different: {result_m1} than your prediction: {result_m2}")