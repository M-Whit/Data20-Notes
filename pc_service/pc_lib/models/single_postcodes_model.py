class SinglePCModel:

    def __init__(self, single_pc_json):
        # In the init method, map out entire data structure into the initialisation of a class
        # Expose the data at each point
        self.status = single_pc_json('status')
        self.result = single_pc_json['result']
        self.postcode = self.result['postcode']
        self.quality = self.result['quality']
        self.eastings = self.result['eastings']
        self.northings = self.result['northings']
        self.country = self.result['country']
        self.nhs_ha = self.result['nhs_ha']
        self.admin_county = self.result['admin_county']
        self.admin_ward = self.result['admin_ward']
        self.longitude = self.result['longitude']
        self.latitude = self.result['latitude']
        self.parliamentary_constituency = self.result['parliamentary_constituency']
        self.european_electoral_region = self.result['european_electoral_region']
        self.primary_care_trust = self.result['primary_care_trust']
        self.region = self.result['region']
        self.parish = self.result['parish']
        self.lsoa = self.result['lsoa']
        self.msoa = self.result['msoa']
        self.ced = self.result['ced']
        self.ccg = self.result['ccg']
        self.nuts = self.result['nuts']
        self.codes = self.result['codes']
        # From here, we access the 'codes' nested dictionary that is in the main bulk of information
        self.codes_admin_district = self.codes['admin_district']
        self.codes_admin_county = self.codes['admin_county']
        self.codes_admin_ward = self.codes['admin_ward']
        self.codes_parish = self.codes['parish']
        self.codes_ccg = self.codes['ccg']
        self.codes_nuts = self.codes['nuts']

        # Before classes we used for cleaning or extraction
        # Here we create an object for the data model, all data within the single postcode call
        # is going to be stored within class attributes
        # 'Service Object Modelling'
        # Can do Object Relational Mapping with SQLchemy using this technique
        # This can then be easily loaded into an SQL database
