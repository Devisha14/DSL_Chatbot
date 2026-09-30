from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Cybersecurity questions
questions = [
    "what is phishing",
    "what is a phishing attack",
    "how does phishing work",
    "how to identify phishing",

    "what is malware",
    "what is malicious software",
    "how to protect against malware",

    "what is ransomware",
    "how does ransomware work",
    "how to protect against ransomware",

    "what is a strong password",
    "how to create a strong password",
    "how to protect my password",
    "password security tips",

    "what is ddos",
    "what is ddos attack",
    "how does ddos attack work",

    "what is identity theft",
    "how to prevent identity theft",

    "what is social engineering",
    "how does social engineering work",

    "how to browse safely",
    "what is safe browsing",
    "internet safety tips",

    "what is two factor authentication",
    "what is 2fa",
    "what is two step verification",
    "why use two factor authentication"
]


# Answers corresponding to the questions
answers = [
    # Phishing
    "Phishing is a cyber attack where attackers use fake emails, messages, or websites to trick people into giving sensitive information such as passwords, OTPs, or bank details.",

    "A phishing attack uses fake emails, messages, or websites to trick users into revealing confidential information.",

    "In phishing, an attacker usually pretends to be a trusted person or organization and sends a fake message containing a malicious link or request for information.",

    "You can identify phishing by checking for suspicious links, unknown senders, spelling mistakes, urgent requests, and requests for passwords or financial information.",

    # Malware
    "Malware means malicious software. It is designed to damage a computer, steal information, or gain unauthorized access to a system.",

    "Malicious software, or malware, includes harmful programs such as viruses, worms, trojans, spyware, and ransomware.",

    "To protect against malware, keep your software updated, use trusted antivirus software, avoid suspicious downloads, and do not open unknown email attachments.",

    # Ransomware
    "Ransomware is a type of malware that encrypts or locks a victim's files and demands money in exchange for restoring access.",

    "Ransomware usually enters a system through malicious links, email attachments, vulnerable software, or compromised websites. It can then encrypt important files.",

    "To protect against ransomware, keep backups, update software, use security software, avoid suspicious links and attachments, and use strong passwords.",

    # Password Security
    "A strong password should be long, unique, and difficult to guess. Use a combination of uppercase letters, lowercase letters, numbers, and special characters.",

    "Create a strong password by using a long combination of letters, numbers, and special characters. Avoid names, birthdays, and common words.",

    "Never share your password with others. Use a different password for each important account and enable two-factor authentication whenever possible.",

    "Password security means protecting passwords from unauthorized access. Use strong and unique passwords, avoid reusing passwords, and enable two-factor authentication.",

    # DDoS
    "A DDoS attack, or Distributed Denial-of-Service attack, attempts to make a website or online service unavailable by sending a very large amount of traffic to it.",

    "A DDoS attack floods a server or website with traffic from many devices, making the service slow or unavailable to legitimate users.",

    "In a DDoS attack, many compromised devices send requests to a target at the same time. This can overload the target's resources and cause service disruption.",

    # Identity Theft
    "Identity theft occurs when someone uses another person's personal information without permission, usually for fraud or other illegal activities.",

    "To prevent identity theft, protect your personal information, use strong passwords, enable two-factor authentication, avoid suspicious websites, and monitor financial accounts.",

    # Social Engineering
    "Social engineering is a cyber attack technique that manipulates people into revealing confidential information or performing unsafe actions.",

    "Social engineering works by exploiting human trust. Attackers may pretend to be employees, banks, friends, or other trusted people to obtain sensitive information.",

    # Safe Browsing
    "Safe browsing means using the internet carefully. Avoid suspicious links, check website addresses, use HTTPS websites, keep your browser updated, and do not download files from unknown sources.",

    "Safe browsing means following security practices while using websites, such as checking URLs, avoiding suspicious links, and not entering sensitive information on untrusted websites.",

    "For internet safety, use strong passwords, enable two-factor authentication, avoid suspicious links, keep software updated, and never share sensitive information with unknown people.",

    # Two-Factor Authentication
    "Two-factor authentication, or 2FA, adds an extra security step after your password. This can be an OTP, authentication-app code, or another verification method.",

    "2FA stands for Two-Factor Authentication. It requires two different types of verification to access an account.",

    "Two-step verification provides an additional security layer. Even if someone gets your password, they may still need the second verification code.",

    "Two-factor authentication improves account security because an attacker needs more than just your password to access the account."
]


# Convert questions into numerical vectors
vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(questions)


def get_response(user_question):

    # Convert user's question into a vector
    user_vector = vectorizer.transform([user_question])

    # Calculate similarity between user's question and stored questions
    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    # Find the most similar question
    best_match = similarity.argmax()

    # Get similarity score
    best_score = similarity[0][best_match]

    # If question is not similar enough
    if best_score < 0.15:

        return (
            "Sorry, I don't understand that question yet. "
            "You can ask me about phishing, malware, ransomware, "
            "password security, DDoS attacks, identity theft, "
            "social engineering, safe browsing, or two-factor authentication."
        )

    # Return the matching answer
    return answers[best_match]