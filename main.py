import config
import BCOSFIRE_media

def main():
    symm_params = config
    symm_params.inputfilter.DoG.sigmalist   = 2.4
    symm_params.COSFIRE.rholist             = [0, 2, 4, 6, 8]
    symm_params.COSFIRE.sigma0              = 3
    symm_params.COSFIRE.alpha               = 0.7

    asymm_params = config
    asymm_params.inputfilter.DoG.sigmalist   = 1.8
    asymm_params.COSFIRE.rholist             = [i for i in range(0,22+1,2)]
    asymm_params.COSFIRE.sigma0              = 2
    asymm_params.COSFIRE.alpha               = 0.1

    image_path = 'data/RETINA_example/01_test.tif'
    BCOSFIRE_media.main(image_path, symm_params, asymm_params, 0.5)


if __name__ == "__main__":
    main()