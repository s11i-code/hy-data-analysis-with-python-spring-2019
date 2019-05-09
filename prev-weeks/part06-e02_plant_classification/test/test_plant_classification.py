#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock


from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import sklearn

from tmc import points

from tmc.utils import load, get_out, patch_helper

module_name="src.plant_classification"
plant_classification = load(module_name, 'plant_classification')
main = load(module_name, "main")
ph = patch_helper(module_name)

# This solution to wrap a patched method comes originally from
# https://stackoverflow.com/questions/25608107/python-mock-patching-a-method-without-obstructing-implementation
def spy_decorator(method_to_decorate):
    mock = MagicMock()
    def wrapper(self, *args, **kwargs):
        mock(*args, **kwargs)
        return method_to_decorate(self, *args, **kwargs)
    wrapper.mock = mock
    return wrapper

@points('p06-02.1')
class PlantClassification(unittest.TestCase):

    
    def test_correctness(self):
        acc = plant_classification()
        self.assertAlmostEqual(acc, 0.966667, places=5, msg="Incorrect accuracy score!")

    def test_accuracy_called(self):
        with patch(ph('sklearn.metrics.accuracy_score'),
                   side_effect=sklearn.metrics.accuracy_score) as accuracy:
            acc = plant_classification()
            accuracy.assert_called_once()

    def test_third(self):
        with patch(ph('sklearn.model_selection.train_test_split'),
                   side_effect=train_test_split) as split:
            acc = plant_classification()
            split.assert_called_once()
            args, kwargs = split.call_args
            self.assertIn('random_state', kwargs,
                          msg="You did not give the random_state argument to"
                          "train_test_split!")
            self.assertEqual(kwargs['random_state'], 0,
                             msg="Incorrect argument value passed to train_test_split function!")
            self.assertIn('train_size', kwargs, msg="You did not give the train_size argument to"
                          "train_test_split!")
            self.assertEqual(kwargs['train_size'], 0.8,
                             msg="Incorrect argument value passed to train_test_split function!")

    def test_gaussian(self):
        predict_method = spy_decorator(sklearn.naive_bayes.GaussianNB.predict)
        fit_method = spy_decorator(sklearn.naive_bayes.GaussianNB.fit)

        with patch.object(sklearn.naive_bayes.GaussianNB, "fit", new=fit_method),\
             patch.object(sklearn.naive_bayes.GaussianNB, "predict", new=predict_method),\
             patch(ph('sklearn.naive_bayes.GaussianNB'),
                   wraps=sklearn.naive_bayes.GaussianNB) as mock_gaussian:
            acc = plant_classification()
            mock_gaussian.assert_called_once()
            
            # Check that fit and predict methods of GaussianNB object are called
            predict_method.mock.assert_called()
            fit_method.mock.assert_called()

if __name__ == '__main__':
    unittest.main()
    
