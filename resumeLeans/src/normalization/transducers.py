from pyformlang.fst import FST

TRANSFORMACIONES = {
    "JS": "JAVASCRIPT", "Javascript": "JAVASCRIPT", "JavaScript": "JAVASCRIPT",
    "TS": "TYPESCRIPT", "Typescript": "TYPESCRIPT", "TypeScript": "TYPESCRIPT",
    "React.js": "REACT", "ReactJS": "REACT", "react": "REACT", "React": "REACT",
    "Angular.js": "ANGULAR", "AngularJS": "ANGULAR", "angular": "ANGULAR", "Angular": "ANGULAR",
    "Vue.js": "VUE", "VueJS": "VUE", "vue": "VUE", "Vue": "VUE",
    "NodeJS": "NODE_JS", "Node.js": "NODE_JS", "node": "NODE_JS", "Node": "NODE_JS",
    "django": "DJANGO", "Django": "DJANGO",
    "Spring Boot": "SPRING_BOOT", "SpringBoot": "SPRING_BOOT", "spring boot": "SPRING_BOOT", "Spring": "SPRING_BOOT",
    "SQL": "SQL", "sql": "SQL",
    "NoSQL": "NOSQL", "nosql": "NOSQL", "No SQL": "NOSQL",
    "Postgres": "POSTGRESQL", "PostgreSQL": "POSTGRESQL", "postgresql": "POSTGRESQL",
    "REST API": "REST_API", "REST APIs": "REST_API", "RESTful API": "REST_API", "rest api": "REST_API",
    "Git": "GIT", "git": "GIT", "GIT": "GIT",
    "Python": "PYTHON", "python": "PYTHON", "py": "PYTHON",
    "pandas": "PANDAS", "Pandas": "PANDAS",
    "numpy": "NUMPY", "NumPy": "NUMPY", "Numpy": "NUMPY",
    "sklearn": "SCIKIT_LEARN", "scikit learn": "SCIKIT_LEARN", "Scikit-learn": "SCIKIT_LEARN",
    "Tensor Flow": "TENSORFLOW", "TensorFlow": "TENSORFLOW", "tf": "TENSORFLOW", "tensorflow": "TENSORFLOW",
    "Py Torch": "PYTORCH", "PyTorch": "PYTORCH", "pytorch": "PYTORCH",
    "ML": "MACHINE_LEARNING", "Machine Learning": "MACHINE_LEARNING", "Machine-learning": "MACHINE_LEARNING", "machine learning": "MACHINE_LEARNING",
    "Docker": "DOCKER", "docker": "DOCKER",
    "Kubernetes": "KUBERNETES", "kubernetes": "KUBERNETES", "K8s": "KUBERNETES", "k8s": "KUBERNETES",
    "Linux": "LINUX", "linux": "LINUX",
    "CI/CD": "CI_CD", "ci/cd": "CI_CD", "CI-CD": "CI_CD", "GitHub Actions": "CI_CD", "GitLab CI": "CI_CD",
    "AWS": "AMAZON_WEB_SERVICES", "Amazon Web Services": "AMAZON_WEB_SERVICES", "amazon web services": "AMAZON_WEB_SERVICES",
    "GCP": "GOOGLE_CLOUD", "Google Cloud": "GOOGLE_CLOUD", "Google Cloud Platform": "GOOGLE_CLOUD",
    "Azure": "AZURE", "Microsoft Azure": "AZURE", "azure": "AZURE",
    "Terraform": "TERRAFORM", "terraform": "TERRAFORM",
    "Apache Spark": "SPARK", "Spark": "SPARK", "spark": "SPARK", "PySpark": "SPARK", "pyspark": "SPARK",
    "Airflow": "AIRFLOW", "airflow": "AIRFLOW", "Apache Airflow": "AIRFLOW",
    "ETL": "ETL", "etl": "ETL", "Extract Transform Load": "ETL",
    "Kafka": "KAFKA", "kafka": "KAFKA", "Apache Kafka": "KAFKA",
    "Data Warehouse": "DATA_WAREHOUSE", "data warehouse": "DATA_WAREHOUSE", "DW": "DATA_WAREHOUSE", "DWH": "DATA_WAREHOUSE"
}

def construir_transducer(diccionario_transformaciones: dict) -> FST:
    """Construye dinámicamente un único FST que contiene todas las rutas de normalización."""
    fst = FST()
    estado_inicial = "q0"
    estado_final = "q_aceptacion"
    
    fst.add_start_state(estado_inicial)
    fst.add_final_state(estado_final)

    contador_estados = 1

    for palabra_cruda, token_salida in diccionario_transformaciones.items():
        estado_actual = estado_inicial
        caracteres_salida = list(token_salida)

        for i, letra in enumerate(palabra_cruda):
            es_ultima_letra = (i == len(palabra_cruda) - 1)
            
            siguiente_estado = estado_final if es_ultima_letra else f"q{contador_estados}"
            salida_transicion = caracteres_salida if es_ultima_letra else []
            
            fst.add_transition(estado_actual, letra, siguiente_estado, salida_transicion)
            
            estado_actual = siguiente_estado
            contador_estados += 1

    return fst

FST_SKILLS = construir_transducer(TRANSFORMACIONES)

def normalizar_skills(datos_crudos_regex: dict) -> list[str]:
    """
    Recibe el diccionario del módulo de regex y retorna una lista ordenada 
    de tokens normalizados usando el FST.
    """
    tokens_normalizados = set()
    
    listas_tecnicas = [
        datos_crudos_regex.get("programming_languages", []),
        datos_crudos_regex.get("frameworks", []),
        datos_crudos_regex.get("databases", []),
        datos_crudos_regex.get("tools", []),
        datos_crudos_regex.get("other_qualifications", [])
    ]
    
    for lista in listas_tecnicas:
        for palabra in lista:
            try:
                resultado = list(FST_SKILLS.translate(list(palabra)))
                if resultado:
                    token = "".join(resultado[0])
                    tokens_normalizados.add(token)
            except Exception:
                pass

    return sorted(list(tokens_normalizados))

if __name__ == "__main__":
    diccionario_simulado = {
        "programming_languages": ["JS", "Python"],
        "frameworks": ["React.js", "tf"],
        "databases": ["Postgres"],
        "tools": ["K8s", "Docker"],
        "other_qualifications": ["machine learning"]
    }
    
    resultado = normalizar_skills(diccionario_simulado)
    print("Salida Normalizada:", resultado)