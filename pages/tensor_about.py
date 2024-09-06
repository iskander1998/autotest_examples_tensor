from selenium.webdriver.common.by import By

class Tensor_About:
    def __init__(self, driver):
        self.driver = driver
    def comparison_picture_sizes_check(self):
        main_image_window = self.driver.find_elements(By.CLASS_NAME, "tensor_ru-About__block3-image-wrapper")
        count_of_equals_windows = 0
        for i in range(len(main_image_window)-1):
            if main_image_window[i].size ==  main_image_window[i+1].size:
                count_of_equals_windows +=1
        assert count_of_equals_windows == len(main_image_window)-1