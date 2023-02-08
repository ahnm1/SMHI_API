from MainSMHI import MainSMHI 


if __name__ == '__main__':
    smhi = MainSMHI()
    smhi.get_raw()
    smhi.get_raw('wind')
    smhi.clean_raw()
    smhi.save_samples('2021-11-01', '2022-10-31')
    smhi.merge_samples()