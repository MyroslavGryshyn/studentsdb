def students_proc(request):
    return {'PORTAL_URL': request.scheme + "://" + str(request.get_host())}
