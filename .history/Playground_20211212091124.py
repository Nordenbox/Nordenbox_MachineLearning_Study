ret_data = {'error_code': 0, 'error_msg': 'SUCCESS', 'log_id': 9994897565050, 'timestamp': 1639269737, 'cached': 0, 'result': {'face_num': 1, 'face_list': [{'face_token': 'c30ea2234f7ecc19c2da086d7a643c31', 'location': {'left': 140.45, 'top': 188.01, 'width': 440, 'height': 430, 'rotation': 6}, 'face_probability': 1, 'angle': {'yaw': -48.34, 'pitch': 4.14, 'roll': 5.61}, 'glasses': {'type': 'sun', 'probability': 0.71}}]}}
glasses = ret_data['result']['face_list'][0]['glasses']

print(glasses)