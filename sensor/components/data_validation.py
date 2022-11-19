






class DataValidation:   
    
    def validate_number_of_columns(self,dataframe:pd.DataFrame)->bool:
        pass

    def is_numerical_column_exist(self,dataframe:pd.DataFrame)->bool:
        pass

    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        pass
    

    def detect_dataset_drift(self,base_df,current_df,threshold=0.05)->bool:
        pass
   

    def initiate_data_validation(self)->DataValidationArtifact:
        pass