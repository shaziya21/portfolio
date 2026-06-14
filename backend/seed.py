from backend.models import Achievement, Education, Experience, Profile, Skill


def seed_database(db):
    if db.query(Profile).first():
        return

    profile = Profile(
        name="Shaziya Akhtar",
        title="Sr. Software Engineer",
        email="shaziyaaa21@gmail.com",
        phone="+91 7389988686",
        github="https://github.com/shaziya21",
        linkedin="https://www.linkedin.com/in/shaziya-akhtar-a22235190/",
        bio="Backend engineer specializing in distributed systems, microservices, and scalable SaaS platforms.",
    )
    db.add(profile)

    skills = [
        "Python", "Microservices", "Postgres", "MySQL", "FastAPI", "Azure",
        "Jenkins", "Docker", "Django", "Git", "MongoDB", "Postman", "DRF",
        "ElasticSearch", "Flask", "Sockets", "AWS", "CI/CD", "REST API",
        "JavaScript", "Bootstrap", "CSS", "HTML", "Architecture", "Jira",
        "Webhooks", "Databases", "Geo-Fencing", "Payments", "Notifications", "Queues",
    ]
    for i, name in enumerate(skills):
        db.add(Skill(name=name, order_index=i))

    experiences = [
        {
            "title": "Sr. Software Developer",
            "company": "Stupa Sports Analytics",
            "location": "Gurugram",
            "start_date": "01/2023",
            "end_date": "Present",
            "description": "Architecting distributed systems for multi-tenant sports SaaS platforms.",
            "highlights": "\n".join([
                "Architected end-to-end distributed notification infrastructure for Email (AWS SES), SMS (AWS SNS), and In-App alerts with Redis rate limiting and DLQ.",
                "Designed scalable multi-tenant, multi-sport SaaS platform for tournament management and live streaming.",
                "Built asynchronous architecture with Celery + Redis for 99.9% API responsiveness during peak hours.",
                "Architected microservices using Docker, Kubernetes, and Jenkins CI/CD with tenant isolation and auto-scaling.",
                "Integrated global payment gateways with end-to-end encryption and refund reconciliation systems.",
                "Developed Self-Registration Module with multi-tenant data isolation and RBAC.",
                "Built fixture generation algorithms (Round Robin, Knockout, Double Round Robin) and dynamic match scheduling.",
                "Integrated YouTube and Mux for OTT live/on-demand streaming with geo-fencing controls.",
                "Led tenant-specific systems for ETTU (Europe), RFETM (Spain), STTA (Sweden), NBTF (Norway), and UTT live scoring via WebSockets.",
            ]),
            "order_index": 5,
        },
        {
            "title": "Software Developer",
            "company": "Momspresso",
            "location": "Gurugram",
            "start_date": "06/2022",
            "end_date": "01/2023",
            "description": "Full-stack backend development for content and campaign platforms.",
            "highlights": "\n".join([
                "Improved performance and responsiveness of the core Momspresso website.",
                "Designed and developed a new Series Module from scratch.",
                "Scaled MyMoney campaign platform to 500K+ active users.",
                "Integrated payment gateways for influencer-brand transactions and cashback workflows.",
                "Engineered 100% cashback logic for MyMo Card influencer system.",
                "Leveraged Elasticsearch, MongoDB, Redis, and PostgreSQL for optimized data access.",
            ]),
            "order_index": 4,
        },
        {
            "title": "Backend Intern",
            "company": "VIGA Entertainment Technology",
            "location": "Gwalior",
            "start_date": "01/2022",
            "end_date": "06/2022",
            "description": "RESTful API development for MovieColab collaborative production pipeline.",
            "highlights": "\n".join([
                "Developed RESTful APIs using Django for cloud-based movie production pipeline.",
                "Built milestone creation, tagging system, and automated notifications using Django signals.",
                "Contributed to centralized dashboard for real-time collaboration.",
            ]),
            "order_index": 3,
        },
        {
            "title": "Backend Intern",
            "company": "Rombits PVT Ltd",
            "location": "Finland (Remote)",
            "start_date": "08/2021",
            "end_date": "01/2022",
            "description": "Backend development for no-code UI customization platform.",
            "highlights": "\n".join([
                "Developed official company website using Django.",
                "Built dynamic UI components with drag-and-drop design and modular customization.",
                "Connected front-end interactions with database-driven features via APIs.",
            ]),
            "order_index": 2,
        },
        {
            "title": "Software Developer Intern",
            "company": "ChefAtHome FoodTech LLP",
            "location": "Bangalore",
            "start_date": "05/2021",
            "end_date": "08/2021",
            "description": "Food delivery platform with role-based dashboards and inventory management.",
            "highlights": "\n".join([
                "Created responsive food delivery website for meal kits and instructional content.",
                "Built Admin, Consumer, and Supplier dashboards with RBAC.",
                "Implemented inventory management with real-time stock updates and low-stock alerts.",
                "Developed RESTful APIs using Django REST Framework.",
            ]),
            "order_index": 1,
        },
        {
            "title": "Java Backend Trainee",
            "company": "Steel Authority Of India Limited",
            "location": "Bhilai",
            "start_date": "03/2020",
            "end_date": "08/2020",
            "description": "Internal blogging platform for organizational communication.",
            "highlights": "Created a blogging website using JSP and Servlets for senior authorities to share orders and ideas.",
            "order_index": 0,
        },
    ]
    for exp in experiences:
        db.add(Experience(**exp))

    education = [
        {
            "degree": "B.Tech — Computer Science & Engineering",
            "institution": "ITM University",
            "location": "Gwalior",
            "start_date": "2018",
            "end_date": "2022",
            "details": "Majors in Computer Science and Engineering",
            "order_index": 1,
        },
        {
            "degree": "Senior Secondary — CBSE (PCM + IP)",
            "institution": "Sr. Sec. School Sec - 4",
            "location": "Bhilai",
            "start_date": "2016",
            "end_date": "2018",
            "details": "CBSE Boards in PCM + IP",
            "order_index": 0,
        },
    ]
    for edu in education:
        db.add(Education(**edu))

    achievements = [
        {
            "title": "Performer of The Year",
            "organization": "Stupa Sports Technology",
            "year": "2024",
            "description": "Awarded for delivering a full-featured Registration Module with advance cart integration, multi-layer verification workflows, and dynamic participant management ahead of schedule.",
            "order_index": 0,
        },
    ]
    for ach in achievements:
        db.add(Achievement(**ach))

    db.commit()
