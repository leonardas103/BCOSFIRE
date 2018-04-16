import config
import BCOSFIRE_media

def main():
    symmfilter = config
    symmfilter.inputfilter.DoG.sigmalist   = 2.4
    symmfilter.COSFIRE.rholist             = [0, 2, 4, 6, 8]
    symmfilter.COSFIRE.sigma0              = 3
    symmfilter.COSFIRE.alpha               = 0.7

    asymmfilter = config
    asymmfilter.inputfilter.DoG.sigmalist   = 1.8
    asymmfilter.COSFIRE.rholist             = [i for i in range(0,22+1,2)]
    asymmfilter.COSFIRE.sigma0              = 2
    asymmfilter.COSFIRE.alpha               = 0.1

    image_path = 'data/RETINA_example/01_test.tif'
    BCOSFIRE_media.main(image_path, symmfilter, asymmfilter, 0.5)


if __name__ == "__main__":
    main()
