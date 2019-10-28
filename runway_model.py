import runway
from runway.data_types import image
from add_mask import Add_mask

@runway.setup(options={})
def setup(opts):
    model = Add_mask()
    return model


@runway.command(name='generate',
                inputs={ 'image': image(channels=3), 'mask': image(channels=4)  },
                outputs={ 'masked_image': image(channels=4) },
                description='Add an alpha mask to an image')
def generate(model, args):
    output_image = model.run_on_input(args['image'], args['mask'])
    return {
        'masked_image': output_image
    }

if __name__ == '__main__':
    runway.run(host='0.0.0.0', port=9001)
