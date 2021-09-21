
import pandas as pd
from sklearn import cluster as cl
import numpy as np
import pytesseract

class Statement():

	def __init__(self, image, row_count, col_count):
		self.image = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT, config='--psm 6')
		self.dim = [row_count, col_count]

	def recognise(self):
		dim = self.dim
		dat = self.image

		storage = np.empty((dim[0], dim[1]), dtype=np.dtype('U500'))
		meta = np.copy(storage)

		text = dat["text"]

		feat_space = [dat["top"], dat['left']]

		estimator = [0, 0]

		_estimator = cl.AgglomerativeClustering(n_clusters=dim[0], linkage='single')
		_estimator.fit(np.array(feat_space[0]).reshape(-1,1))

		estimator[0] = _estimator

		_estimator = cl.AgglomerativeClustering(n_clusters=dim[1], linkage='single')
		_estimator.fit(np.array(feat_space[1]).reshape(-1,1))

		estimator[1] = _estimator


		for i in range(len(text)):
			k = estimator[0].labels_[i]
			j = estimator[1].labels_[i]


			if not text[i] in ['']:
				if storage[k, j] == '':
					storage[k, j] = text[i]
				else:
					storage[k, j] = ' '.join([storage[k, j], text[i]])


		for d in range(len(dim)):

			dest = [slice(None)] * len(dim)
			sour = [slice(None)] * len(dim)

			eq = {}

			for i in range(dim[d]):
				ind = list(estimator[d].labels_).index(i)
				eq[feat_space[d][ind]] = i

			sorted_keys = sorted(eq.keys())


			i = 0


			for key in sorted_keys:
				dest[d] = i
				sour[d] = eq[key]

				meta[tuple(dest)] = storage[tuple(sour)]
				i += 1	


			storage = np.copy(meta)

		self.output = storage

	def store(self, location = 'my_excel_file.xlsx'):
		df = pd.DataFrame(self.output)
		df.to_excel(location, index=False)
