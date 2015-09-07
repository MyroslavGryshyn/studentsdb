def students_proc(request):
    #s = str(request.scheme) + '://' + str(request.get_host)
    return {'PORTAL_URL': request.scheme + "://" + str(request.get_host())}
