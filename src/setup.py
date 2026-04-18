from setuptools import setup
import setup_translate

pkg = 'Extensions.MovieManager'
setup(name='enigma2-plugin-extensions-moviemanager',
       version='2.02',
       description='copy, move and delete more files at once',
       package_dir={pkg: 'MovieManager'},
       packages=[pkg],
       package_data={pkg: ['png/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
