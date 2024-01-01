def get_client_ip(request):
    """
    get client ip
    """
    # Check if the request has an 'HTTP_X_FORWARDED_FOR' header
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        # If the header is present, extract the IP address from the comma-separated list
        ip = x_forwarded_for.split(',')[0]
    else:
        # If the header is not present, use the 'REMOTE_ADDR' value from the request's META data
        ip = request.META.get('REMOTE_ADDR')

    # Return the IP address
    return ip
