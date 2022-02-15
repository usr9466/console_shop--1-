from classes.views.main_view import MainView

'''
    the main function, will be called by shell or bash
'''
if __name__ == '__main__':
    # create the ui
    main_view = MainView('base ui view')

    # start ui
    main_view.main_loop()