# -*- coding: utf-8 -*-
"""Untitled28.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18zY_i4kAuNGAN-ToogMB_EyFPb97136E
"""

import google.colab.files, json, joblib, matplotlib.pyplot as plt, requests, sklearn.metrics, sklearn.model_selection, sklearn.tree

response = requests.get("https://dgoldberg.sdsu.edu/515/kiva_data_full.json")

if response:
    data = json.loads(response.text)

    x = []
    y = []


    for line in data:
        length = line["length"]
        loanstatus = line["loan_status"]
        numberofpicture = line["number_of_pictures"]
        loanamount = line["loan_amount"]
        bounscrediteligibility = line["bonus_credit_eligibility"]
        userfavoritepost = line["user_favorite_post"]
        inner_list = [length, numberofpicture, loanamount]

        if userfavoritepost == "yes":
            inner_list.append(1)
        else:           
            inner_list.append(0)
        
        if bounscrediteligibility == "yes":
            inner_list.append(1)
        else:           
            inner_list.append(0)
               
        x.append(inner_list)

        y.append(loanstatus)

    # Split x and y into training and test
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.3, random_state = 0)

    # Train decision tree
    clf = sklearn.tree.DecisionTreeClassifier()
    clf = clf.fit(x_train, y_train)

    # Assess accuracy
    predictions = clf.predict(x_test)
    accuracy = sklearn.metrics.accuracy_score(y_test, predictions)
    print("Accuracy:", accuracy)

    # Show a visual confusion matrix
    cm = sklearn.metrics.confusion_matrix(y_test, predictions)
    disp = sklearn.metrics.ConfusionMatrixDisplay(cm)
    disp.plot()
    plt.show()

    # Export decision tree model using joblib
    joblib.dump(clf, "kiva_decision_tree.joblib")
    google.colab.files.download("kiva_decision_tree.joblib")
    print("Decision tree model saved to kiva_decision_tree.joblib.")

else:
    print("Sorry, connection error.")

import joblib, sklearn.metrics, sklearn.tree


# Load decision tree model from joblib file
filename = input("Enter the name of the decision tree file to load:")
if filename == "kiva_decision_tree.joblib":
    x1 = []
    y = []
    inner_list1 = []
    yes = 1
    no = 0
    length = input("Enter the length of the post to predict:")
    inner_list1.append(length)
    numberofpicture = input("Enter the number of pictures in the post:")
    inner_list1.append(numberofpicture)
    loanamount = input("Enter the loan amount requested:")
    inner_list1.append(loanamount)
    bounscrediteligibility = input("Enter the bonus credit eligibility (yes/no):").lower()
    if bounscrediteligibility == "yes":
        inner_list1.append(1)
    else:           
        inner_list1.append(0)
    userfavoritepost = input("Enter whether the post was a user favorite post (yes/no):").lower()
    if userfavoritepost == "yes":
        inner_list1.append(1)
    else:           
        inner_list1.append(0)



    x1.append(inner_list1)
    y.append(loanstatus)
    clf = joblib.load(filename)
    predictions = clf.predict(x1)
    if predictions == "funded":
        print(predictions)
    else:
        print("Based on the decision tree, the loan will not be funded.")
else:
    print("Sorry, connetion error.")