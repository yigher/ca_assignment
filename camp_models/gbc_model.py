"""sgd_model.py"""
import pickle
import warnings
import numpy as np
warnings.filterwarnings("ignore")
from camp_utils.survey_util import Util
from camp_models.abstract_model import AbstractModel
from sklearn.ensemble import GradientBoostingClassifier
from camp_models.doc2vec_model import Doc2VecModel
from sklearn.model_selection import train_test_split
from camp_data_parser.doc2vec_to_np_data_parser import Doc2VecToNumpyDataParser
from sklearn.preprocessing import scale

class GBClassModel(AbstractModel):
    """GBClassModel"""
    def __init__(
            self,
            train_val_split=0.2):
        """__init__"""
        self.model = None
        self.train_val_split = train_val_split

    def fit(self, inputs):
        """fit method
        inputs = list of x and y numpy array"""
        x_all = inputs[0]
        y_all = inputs[1]
        x_train, x_val, y_train, y_val = train_test_split(x_all, y_all, test_size=self.train_val_split)
        x_train = scale(x_train)
        x_val = scale(x_val)
        self.model = GradientBoostingClassifier(n_estimators=400, learning_rate=1.0)
        self.model = self.model.fit(x_train, y_train)
        print('Test Accuracy: %.2f' % self.model.score(x_val, y_val))
        return self.model

    def predict(self, inputs):
        """predict
         inputs = numpy array of sentence vector representation
         returns
            pred_probas = probabilities of the labels"""
        inputs = scale(inputs)
        pred_probas = self.model.predict_proba(inputs)
        return pred_probas

    def save(self, file_location):
        """save model method
        file_location = string file location"""
        with open(file_location, 'wb') as f_out:
            pickle.dump(self.model, f_out)

    def load(self, file_location):
        """load model method
        file_location = string file location
        returns
            model = GradientBoostingClassifier"""
        with open(file_location, 'rb') as f_out:
            self.model = pickle.load(f_out)
        return self.model

if __name__ == "__main__":
    DOC2VEC_MODEL = Doc2VecModel()
    MODEL = DOC2VEC_MODEL.load("../model_files/DOC2VEC_MODEL.doc2vec")
    DATA_PARSER = Doc2VecToNumpyDataParser(MODEL)
    X_OUT, Y_OUT, Y_DICT, Y_REV_DICT = DATA_PARSER.convert()
    print("x_out shape: ", X_OUT.shape)
    print("y_out shape: ", Y_OUT.shape)
    print("y_dict: ", Y_DICT)
    print("y_reverse_dict: ", Y_REV_DICT)
    MODEL_OUT = GBClassModel()
    MODEL_OUT.fit([X_OUT, Y_OUT])
    print(MODEL_OUT.predict(X_OUT[10]))

