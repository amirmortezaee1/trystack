def jsonify(state={}, metadata={}, headers={}, status=200):
     resource = {}
     resource.update(state)
     resource.update(metadata)
     return resource, status, headers