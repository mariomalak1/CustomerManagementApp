from django.shortcuts import render

def handelError(request, error_name):
    print(error_name == "403")
    if error_name == "403":
        message_error = "you don't have permission to do that"
    elif error_name == "404":
        message_error = "Page Not Found"
    elif error_name == "500":
        message_error = "we are experiencing some trouble on our end. please try again near future"
    else:
        message_error = "Error Happen"
    context = {"message_error":message_error,
               "error_name":error_name}
    return render(request, "errorsApp/errorPage.html", context)