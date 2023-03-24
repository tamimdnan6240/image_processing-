for class_name in ["DME", "DRUSEN"]:
    for img in os.listdir(train_dir + "/" + class_name):
        img_array = cv2.imread(train_dir + "/" + class_name + "/" + img)
        
        img_array = cv2.resize(img_array, (128,128))
        lr_img_array = cv2.resize(img_array,(32,32))
        cv2.imwrite(train_dir+ "/hr_images/" + class_name + "_" + img, img_array)
        cv2.imwrite(train_dir+ "/lr_images/" + class_name + "_" + img, lr_img_array)
