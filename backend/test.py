from ApiService import ApiService

if __name__ == "__main__":
    service = ApiService()
    result = service.fetch("Tashkent")
    print(result)
