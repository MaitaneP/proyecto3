# project-da-promo-D-module-3-team-1
Este repositorio incluye el proyecto del equipo 1 del Módulo 3 de la promo D del bootcamp de Data Analytics de Adalab. El nombre del equipo es Reading the Future y las integrantes son Estibaliz Gallego, Iris Herrero, Cristina Bernabeu y Maitane Portilla.

**OBJETIVO:**

Desarrollo de un modelo de machine learning para una empresa de alquiler de bicicletas, considerando ususarios registrados y casuales.

**DESARROLLO:**

1.1 EXPLORACIÓN:  
En primer lugar hemos procedido a realizar la exploración del dataset tanto de forma analítica como numérica. Entre las actividades más importantes destacan:
- Selección de la variable respuesta
- Renombrado de columnas
- Cambio de tipo de datos
- Análisis de las variables categóricas y numéricas en relación a la variable respuesta
- Correlación entre las variables numéricas, eliminación de columnas redundantes
- Gestión de outliers
- Guardado del dataset modificado

1.2. PROCESADO:
- Intento de normalización de la variable respuesta -> descartamos el algoritmo de regresión lineal
- Estandarización de variables numéricas
- Encoding de variables categóricas

1.3. MODELOS DE DECISION TREE
- Separado de los datos en X e y, train y test
- Entrenamiento y ajuste del modelo
- Estimación del mejor modelo
- Matriz de confusión
- Métricas
- Importancia de las variables predictoras
- Comparación con otros modelos

1.4. MODELOS DE RANDOM FOREST
- Separado de los datos en X e y, train y test
- Entrenamiento y ajuste del modelo
- Estimación del mejor modelo
- Matriz de confusión
- Métricas
- Importancia de las variables predictoras
- Comparación con otros modelos

**RESULTADOS:**
Modelo Casual: R2: 0,784; RMSE: +- 322 
Modelo Registered: R2: 0,865; RMSE: +- 541

Tras la diversas pruebas realizadas nos quedamos para ambos casos (casuales y registrados) con modelos predictores basados en 6 variables, conseguimos métricas mejores y aportamos simplicidad y explicabilidad.

Siendo los usuarios registrados totales muy superiores a los casuales es coherente que su margen de error en términos absolutos sea mayor. Si analizamos este error en porcentaje encontramos que el de registrados es de solo un 7,81%, mientras que el de casuales es de 9,45%.

**ORGANIZACIÓN DEL REPOSITORIO:**
La documentación se ha organizado en las siguientes carpetas y archivos:
- [**datos:**](https://github.com/Adalab/project-da-promo-D-module-3-team-1/tree/main/datos) Contiene los archivos con los datos de partida de origen, los datos tratados en sus distintas fases de limpieza y tratado y los resultados (mejores modelos).
- [**web:**](https://github.com/Adalab/project-da-promo-D-module-3-team-1/tree/main/web) Incluye todos los archivos para el desarrollo de la web y la automatización de la predicción.
- [**1_reconocimiento_inicial.ipynb:**](https://github.com/Adalab/project-da-promo-D-module-3-team-1/blob/main/1_reconocimiento_inicial.ipynb) Recoge los trabajos de reconocimiento y exploración inicial del dataset.
- [**2_asunciones.ipynb:**](https://github.com/Adalab/project-da-promo-D-module-3-team-1/blob/main/2_asunciones.ipynb) Incluye el análisis de las asunciones para regresión lineal.
- [**3_estandarizacion.ipynb:**](https://github.com/Adalab/project-da-promo-D-module-3-team-1/blob/main/3_estandarizacion.ipynb) Recoge las tareas de estandarización de las variables predictoras.
- [**4.1_encoding.ipynb:**](https://github.com/Adalab/project-da-promo-D-module-3-team-1/blob/main/4.1_encoding.ipynb) Contiene las tareas de encoding de las variables predictoras en el dataset sin estandarizar.
- [**4.2_encoding_con_estandarizacion.ipynb:**](https://github.com/Adalab/project-da-promo-D-module-3-team-1/blob/main/4.2_encoding_con_estandarizacion.ipynb) Recoge las tareas de encoding de las variables predictoras en el dataset estandarizado.
- [**5.1_modelo_casual1.ipynb:**](https://github.com/Adalab/project-da-promo-D-module-3-team-1/blob/main/5.1_modelo_casual1.ipynb) Contiene los modelos con las variables sin estandarizar de tipo casual.
- [**5.1_modelo_registered1.ipynb:**](https://github.com/Adalab/project-da-promo-D-module-3-team-1/blob/main/5.1_modelo_registered1.ipynb) Contiene los modelos con las variables sin estandarizar de tipo registered.
- [**5.2_modelo_casual1_est.ipynb:**](https://github.com/Adalab/project-da-promo-D-module-3-team-1/blob/main/5.2_modelo_casual1_est.ipynb) Contiene  los modelos con las variables estandarizadas de tipo casual.
- [**5.2_modelo_registered1_est.ipynb:**](https://github.com/Adalab/project-da-promo-D-module-3-team-1/blob/main/5.2_modelo_registered1_est.ipynb) Contiene  los modelos con las variables estandarizadas de tipo registered.
- [**5.3_modelo_casual1_est_princ.ipynb:**](https://github.com/Adalab/project-da-promo-D-module-3-team-1/blob/main/5.3_modelo_casual1_est_princ.ipynb) Contiene  los modelos con las variables estandarizadas de tipo casual, una vez reducidas las variables predictoras.
- [**5.3_modelo_registered1_est_princ.ipynb:**](https://github.com/Adalab/project-da-promo-D-module-3-team-1/blob/main/5.3_modelo_registered1_est_princ.ipynb) Contiene  los modelos con las variables estandarizadas de tipo registered, una vez reducidas las variables predictoras.
- [**esquema.md:**](https://github.com/Adalab/project-da-promo-D-module-3-team-1/blob/main/esquema.md) Esquema de la presentación al cliente.

**LIBRERÍAS:**

A continuación se incluye un listado de las librerías utilizadas:  
- [pandas](https://pandas.pydata.org/)  
- [numpy](https://numpy.org/)  
- [warnings](https://docs.python.org/3/library/warnings.html)    
- [sys](https://docs.python.org/3/library/sys.html)  
- [matplotlib](https://matplotlib.org/)  
- [seaborn](https://seaborn.pydata.org/)  
- [sklearn](https://scikit-learn.org/stable/)  
- [pickle](https://docs.python.org/3/library/pickle.html)
- [holidays](https://pandas.pydata.org/pandas-docs/version/0.17/timeseries.html#timeseries-holiday)
- [scipy](https://scipy.org/)  
- [statsmodels](https://www.statsmodels.org/stable/index.html)    
- [researchpy](https://pypi.org/project/researchpy/)    
- [math](https://docs.python.org/3/library/math.html) 
- [tqdm](https://pypi.org/project/tqdm/)  

