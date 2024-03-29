import pprint 
ret_data = {'cached': 0,
 'error_code': 0,
 'error_msg': 'SUCCESS',
 'log_id': 5515843520179,
 'result': {'face_list': [{'age': 34,
                           'angle': {'pitch': -1.46,
                                     'roll': -13.48,
                                     'yaw': 6.75},
                           'face_probability': 1,
                           'face_token': '1ae62eb83ac03f33ad582ee78e316b09',
                           'glasses': {'probability': 1, 'type': 'common'},
                           'location': {'height': 583,
                                        'left': 183.62,
                                        'rotation': -13,
                                        'top': 301.4,
                                        'width': 609},
                           'quality': {'blur': 0,
                                       'completeness': 1,
                                       'illumination': 53,
                                       'occlusion': {'chin_contour': 0.01,
                                                     'left_cheek': 0.01,
                                                     'left_eye': 0.01,
                                                     'mouth': 0,
                                                     'nose': 0,
                                                     'right_cheek': 0,
                                                     'right_eye': 0}}},
                          {'age': 36,
                           'angle': {'pitch': -3.33,
                                     'roll': -2.64,
                                     'yaw': 17.72},
                           'face_probability': 1,
                           'face_token': 'c1b38ecc6117a95ab50ff729d543e5de',
                           'glasses': {'probability': 0.73, 'type': 'none'},
                           'location': {'height': 543,
                                        'left': 1406.7,
                                        'rotation': -3,
                                        'top': 1208.98,
                                        'width': 544},
                           'quality': {'blur': 0,
                                       'completeness': 1,
                                       'illumination': 47,
                                       'occlusion': {'chin_contour': 0.16,
                                                     'left_cheek': 0.07,
                                                     'left_eye': 0.94,
                                                     'mouth': 0,
                                                     'nose': 0.1,
                                                     'right_cheek': 0.03,
                                                     'right_eye': 0}}},
                          {'age': 32,
                           'angle': {'pitch': 8.46, 'roll': 3.48, 'yaw': 50.09},
                           'face_probability': 1,
                           'face_token': 'ebfd242f0415bffa58183137ecec2158',
                           'glasses': {'probability': 1, 'type': 'common'},
                           'location': {'height': 496,
                                        'left': 668.19,
                                        'rotation': 6,
                                        'top': 1298.17,
                                        'width': 519},
                           'quality': {'blur': 0.98,
                                       'completeness': 1,
                                       'illumination': 57,
                                       'occlusion': {'chin_contour': 0.04,
                                                     'left_cheek': 0.92,
                                                     'left_eye': 0.78,
                                                     'mouth': 0.01,
                                                     'nose': 0.06,
                                                     'right_cheek': 0,
                                                     'right_eye': 0.69}}},
                          {'age': 30,
                           'angle': {'pitch': 11.58,
                                     'roll': -2.71,
                                     'yaw': -10.32},
                           'face_probability': 1,
                           'face_token': '5a34911f50edf6bb6702fa484ce42dae',
                           'glasses': {'probability': 0.53, 'type': 'sun'},
                           'location': {'height': 483,
                                        'left': 2783.38,
                                        'rotation': -3,
                                        'top': 1475.94,
                                        'width': 530},
                           'quality': {'blur': 0,
                                       'completeness': 1,
                                       'illumination': 68,
                                       'occlusion': {'chin_contour': 0.01,
                                                     'left_cheek': 0.01,
                                                     'left_eye': 1,
                                                     'mouth': 0,
                                                     'nose': 0.08,
                                                     'right_cheek': 0.04,
                                                     'right_eye': 0.79}}},
                          {'age': 28,
                           'angle': {'pitch': 3.57,
                                     'roll': 4.58,
                                     'yaw': -45.59},
                           'face_probability': 1,
                           'face_token': '1e5e7e0990e8177b6513d4d61ff1798b',
                           'glasses': {'probability': 0.61, 'type': 'sun'},
                           'location': {'height': 493,
                                        'left': 1471.29,
                                        'rotation': 3,
                                        'top': 272.63,
                                        'width': 511},
                           'quality': {'blur': 0.01,
                                       'completeness': 1,
                                       'illumination': 79,
                                       'occlusion': {'chin_contour': 0,
                                                     'left_cheek': 0,
                                                     'left_eye': 0.95,
                                                     'mouth': 0,
                                                     'nose': 0.14,
                                                     'right_cheek': 0.5,
                                                     'right_eye': 1}}},
                          {'age': 25,
                           'angle': {'pitch': 19.31,
                                     'roll': -2.86,
                                     'yaw': 63.42},
                           'face_probability': 1,
                           'face_token': '92bd61bb6b9a4adab146a8b15a0b503c',
                           'glasses': {'probability': 0.61, 'type': 'none'},
                           'location': {'height': 454,
                                        'left': 3104.26,
                                        'rotation': 0,
                                        'top': 285.3,
                                        'width': 351},
                           'quality': {'blur': 0.05,
                                       'completeness': 1,
                                       'illumination': 29,
                                       'occlusion': {'chin_contour': 0.34,
                                                     'left_cheek': 0.46,
                                                     'left_eye': 0.04,
                                                     'mouth': 0.45,
                                                     'nose': 0.11,
                                                     'right_cheek': 0.41,
                                                     'right_eye': 0.3}}},
                          {'age': 22,
                           'angle': {'pitch': 8.7, 'roll': 3.26, 'yaw': -43.05},
                           'face_probability': 0.99,
                           'face_token': '77e3e2224b4791f97838755e0755ef75',
                           'glasses': {'probability': 1, 'type': 'none'},
                           'location': {'height': 201,
                                        'left': 2400.61,
                                        'rotation': 6,
                                        'top': 434.3,
                                        'width': 176},
                           'quality': {'blur': 0.98,
                                       'completeness': 1,
                                       'illumination': 100,
                                       'occlusion': {'chin_contour': 0,
                                                     'left_cheek': 0.26,
                                                     'left_eye': 0.8,
                                                     'mouth': 0,
                                                     'nose': 0,
                                                     'right_cheek': 0.6,
                                                     'right_eye': 0.2}}}],
            'face_num': 7},
 'timestamp': 1639283195}

for i in ret_data['result']['face_list']:
    pprint.pprint(i[0])