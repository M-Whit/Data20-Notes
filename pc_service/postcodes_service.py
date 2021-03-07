from pc_lib.single_pc import SinglePC


class PostcodesDataService:

    def single_postcode_data(self, postcode):
        return SinglePC(postcode)


postcode = PostcodesDataService().single_postcode_data('se120nb')
print(postcode)
