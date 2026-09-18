def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"  
        case 500:
            return "internal server error"
        case _:
            return "unknown status" 


print(http_status(200))  # Output: ok
print(http_status(404))  # Output: not found
print(http_status(500))  # Output: internal server error
print(http_status(403))  # Output: unknown status