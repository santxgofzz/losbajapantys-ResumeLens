from pyformlang.fst import FST

TRANSFORMACIONES = {
    "Java": "JAVA", "MySQL": "MYSQL", "MongoDB": "MONGODB",
    "RESTful APIs": "REST_API",
    "machine learning model development": "MACHINE_LEARNING",
    "machine-learning model development": "MACHINE_LEARNING",
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
    "CI/CD": "CI_CD",
    "ci/cd": "CI_CD",
    "CI-CD": "CI_CD",

    "GitHub Actions": "GITHUB_ACTIONS",
    "Github Actions": "GITHUB_ACTIONS",
    "github actions": "GITHUB_ACTIONS",

    "GitLab CI": "GITLAB_CI",
    "Gitlab CI": "GITLAB_CI",
    "gitlab ci": "GITLAB_CI",

    "Jenkins": "JENKINS",
    "jenkins": "JENKINS",
    "JENKINS": "JENKINS",

    "AWS": "AWS",
    "aws": "AWS",
    "Amazon Web Services": "AWS",
    "amazon web services": "AWS",

    "GCP": "GCP",
    "gcp": "GCP",
    "Google Cloud": "GCP",
    "google cloud": "GCP",
    "Google Cloud Platform": "GCP",
    "google cloud platform": "GCP",

    "Azure": "AZURE",
    "Microsoft Azure": "AZURE",
    "azure": "AZURE",
    "Terraform": "TERRAFORM", "terraform": "TERRAFORM",
    "Apache Spark": "SPARK", "Spark": "SPARK", "spark": "SPARK", "PySpark": "SPARK", "pyspark": "SPARK",
    "Airflow": "AIRFLOW", "airflow": "AIRFLOW", "Apache Airflow": "AIRFLOW",
    "ETL": "ETL", "etl": "ETL", "Extract Transform Load": "ETL",
    "Kafka": "KAFKA", "kafka": "KAFKA", "Apache Kafka": "KAFKA",
    "Data Warehouse": "DATA_WAREHOUSE", "data warehouse": "DATA_WAREHOUSE", "DW": "DATA_WAREHOUSE", "DWH": "DATA_WAREHOUSE"
}

def construir_transducer(diccionario_transformaciones: dict) -> FST:
    """Build one FST with case variants and horizontal whitespace transitions.

    Each alias has its own route; only its final transition emits the token.
    Spaces in aliases accept one or more spaces/tabs. Input is never rewritten.
    """
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
            
            variantes = {letra.lower(), letra.upper()} if letra.isascii() and letra.isalpha() else {letra}
            if letra == " ":
                variantes = {" ", "\t"}
            for variante in sorted(variantes):
                fst.add_transition(estado_actual, variante, siguiente_estado, salida_transicion)
                if letra == " ":
                    fst.add_transition(siguiente_estado, variante, siguiente_estado, [])
            
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
            resultado = next(FST_SKILLS.translate(list(palabra)), None)
            if resultado is not None:
                tokens_normalizados.add("".join(resultado))

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
