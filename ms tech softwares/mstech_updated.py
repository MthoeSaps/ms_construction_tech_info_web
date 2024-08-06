import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image
from twilio.rest import Client

# Set the page configuration
st.set_page_config(page_title="Mthoe Saps Construction Technologies", layout="wide")
with st.sidebar:
        image = Image.open("ms tech softwares/vids and img/logo3.png")
        st.image(image, use_column_width=False, width=250)
# Define the pages
def home_page():
    # Add the header
    st.title("MS Construction Tech🚧")
    st.subheader("Technovative Land Development SaaS company")
    st.divider()
    # Add the company information
    st.info("Mthoe Saps Construction Technologies is an innovative technology company based in Bulawayo, Zimbabwe. We specialize in developing innovative software solutions for a wide range of industries.")
        # Add the software solutions
    st.header("Our Software Solutions")
    with st.expander("Terra Vista: Bulawayo Mapping Engine 🌍", expanded=False):
        st.write("Terra Vista is our cutting-edge mapping engine that provides detailed and accurate maps of Bulawayo. It utilizes the latest GIS and remote sensing technologies to deliver comprehensive spatial data analysis and visualization.")
        coz1, coz2 = st.columns(2)
        if st.button("Preview Terra Vista"):
            with coz1:
                st.write("Here are some key features of Terra Vista:")
                st.write("- High-resolution satellite imagery for detailed mapping")
                st.write("- Integrated GIS tools for spatial analysis and data visualization")
                st.write("- Customizable map layers and data overlays")
                st.write("- Real-time updates for optimal decision-making")
            with coz2:
                video_file = open('ms tech softwares/vids and img/logo2.mp4', 'rb')
                video_bytes = video_file.read()
                st.video(video_bytes, start_time= 0 ,loop=True)

    # [Additional software solution details omitted for brevity]
     
    
    st.header("Other Software Solutions")
    with st.expander("Other software solutions info 📚", expanded=False):
        st.write("In addition to our flagship products, we also offer a wide range of other software services.")
        if st.button("Preview Other Software Solutions"):
            coz1, coz2 = st.columns(2)
            with coz1:
                st.write("Our other software solutions include:")
                st.write("- POS systems")
                st.write("- Inventory Management systems")
                st.write("- Online ticket sales platforms")
                st.write("- Taxi rank Management systems")
                st.write("- School and hospital management systems")
                st.write("- Sport performance systems")
                st.write("- eCommerce stores")
                st.write("- Fitness and gym management services")
                st.write("- Security and cyber security services")

            with coz2:
                with st.container(border=False):
                    video_file = open('ms tech softwares/vids and img/logo4.mp4', 'rb')
                    video_bytes = video_file.read()
                    st.video(video_bytes, start_time= 0 ,loop=True)
    # Add the footer
    st.write("---")
    st.write(f"© {datetime.now().year} Mthoe Saps Construction Technologies. All rights reserved.")
    
def enquiry_page():
    st.title("Make an Enquiry 📥")
    st.info("Fill out this form to make an enquiry with us and we will get back to you ASAP.")

    # Get user input
    full_name = st.text_input("Full Name")
    surname = st.text_input("Surname")
    company_name = st.text_input("Company Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    province = st.selectbox("Province", ["Bulawayo", "Harare", "Mashonaland Central", "Mashonaland East", "Mashonaland West", "Matabeleland North", "Matabeleland South", "Midlands", "Masvingo"])
    address = st.text_input("House Address")
    services = st.multiselect("Select Preferred Services", ["Terra Vista", "Spatial Data Analysis", "GIS and Remote Sensing", "Machine Learning and AI", "POS Systems", "Inventory Management", "Online Ticket Sales", "Taxi Rank Management", "School and Hospital Management", "Sport Performance", "eCommerce", "Fitness and Gym Management", "Security and Cyber Security"])

    # Define the pricing for each service
    pricing = {
        "Terra Vista": 790,
        "Spatial Data Analysis": 260,
        "GIS and Remote Sensing": 400,
        "Machine Learning and AI": 600,
        "POS Systems": 100,
        "Inventory Management": 150,
        "Online Ticket Sales": 200,
        "Taxi Rank Management": 250,
        "School and Hospital Management": 300,
        "Sport Performance": 150,
        "eCommerce": 250,
        "Fitness and Gym Management": 200,
        "Security and Cyber Security": 400,
        "Animated Graphic Designing": 80
    }

    # Calculate the total charge
    total_charge = sum([pricing[service] for service in services])

    # Display the total charge
    st.write(f"Total Software Licence Charge: ${total_charge:.2f}")

    # Add the submit button
    if st.button("Submit Enquiry"):
        # Create a new row in the Excel file
        data = {
            "Full Name": full_name,
            "Surname": surname,
            "Company Name": company_name,
            "Email": email,
            "Phone Number": phone,
            "Province": province,
            "Address": address,
            "Services": ", ".join(services),
            "Total Charge": total_charge,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Load the existing Excel file or create a new one if it doesn't exist
        try:
            df = pd.read_excel("ms tech softwares/databases/enquiries.xlsx")
        except FileNotFoundError:
            df = pd.DataFrame(columns=list(data.keys()))

        # Add the new row to the DataFrame and save it to the Excel file
        df.loc[len(df)] = data
        df.to_excel("ms tech softwares/databases/enquiries.xlsx", index=False)

        # Send a notification using Twilio
        account_sid = "AC29f22d5739c2440f68af3eec1062a026"
        auth_token = "21f5e303f5eec50e09ebab0f607a4761"
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body=f"Mthoe Saps Construction Technologies, New enquiry received from {full_name} {surname}, email: ({email}) residing at({address}), {province}, ({phone}), enquiries total {total_charge}, enquired at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} for the following services: {', '.join(services)}.",
                            from_="+19148613934",
                            to="+263777932721"
                        )

        print(message.sid)

        st.write(f"Thank you, {full_name}. We will get back to you shortly regarding your enquiry for the following services: {', '.join(services)}.")

        # Display a success message
        st.success("Your enquiry has been submitted successfully!")

# Create the sidebar navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to:", ["Home🏠", "Enquiry📩", "FAQ(s)/ About us❓"])


with st.sidebar:
    with st.container(border=True):
        st.subheader("Get in touch with us📞", divider=True)
        selected_option = st.selectbox("Select Contact Method", ["WhatsApp", "LinkedIn", "Instagram"])
        if selected_option == "WhatsApp":
            st.info("Use the following buttons to get in touch with us:")
            st.link_button("WhatsApp Us", "https://wa.me/263777932721")
        if selected_option == "LinkedIn":
            st.info("You can visit our LinkedIn profile and check our work, you can also contact us from there")
            st.link_button("View our Linkedln Profile", "https://www.linkedin.com/in/mthokozisi-sapuwa-1ab2151ab?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")
        if selected_option == "Instagram":
            st.info("Find us on IG too")
            st.link_button("Instagram Chat", "https://www.instagram.com/mthoe_saps_construction_tech?igsh=MWZibnVpOWZkcmcyNg==")


def about_page():
    st.title("Frequently Asked Questions ❔")
    with st.expander("What services does Mthoe Saps Construction Technologies offer?"):
        st.write("""
                 Mthoe Saps Construction Technologies is a SaaS company based in Bulawayo, Zimbabwe that specializes in geospatial data analysis, remote sensing, and custom software development. We offer a range of services including:

    - GIS and spatial data analysis 📊
    - Remote sensing and satellite imagery processing 📡
    - Streamlining workflows and processes through custom software development 🔗
    - Providing software solutions for a variety of industries, not just construction
                 """)

    with st.expander("What industries do you serve?"):
        st.write("""
    While our roots are in the construction industry, we cater to clients across many different sectors, including:

    - Construction 🏗👷‍♂️
    - Real estate 🏨
    - Urban planning 🌆
    - Agriculture🌾🐄
    - Mining ⛏
    - Environmental conservation 🏞
    - And more!
                 """)

    with st.expander("How can I get started with your services?"):
        st.write("""
    To get started, you can reach out to us through our website or by email. One of our representatives will be happy to discuss your specific needs and requirements, and provide more information about our capabilities and pricing.
        """)

    with st.expander("What technologies do you use?"):
        st.write("""
    At the core of our solutions are Python data science libraries, which allow us to rapidly build and deploy custom web applications. We also leverage a variety of geospatial data tools and techniques, including remote sensing, GIS software, and spatial data analysis.
        """)

    with st.expander("Do you offer any support or training?"):
        st.write("""
    Absolutely. We understand that working with new technologies and software can be daunting, which is why we provide comprehensive support and training to all of our clients. This includes onboarding, documentation, and ongoing assistance to ensure you get the most out of our solutions.
        """)

    st.header("About Us")

    st.write("""
Mthoe Saps Construction Technologies is a leading SaaS company based in Bulawayo, Zimbabwe. We specialize in developing innovative solutions that leverage the power of geospatial data and custom software to help our clients streamline their workflows and processes.

Our team of highly skilled developers, data analysts, and domain experts are passionate about pushing the boundaries of what's possible with technology. We're constantly exploring new techniques and tools, like remote sensing and GIS, to create cutting-edge solutions for our clients.

But what sets us apart is our commitment to understanding our clients' unique needs and challenges. We don't just offer off-the-shelf products – we work closely with each client to design and build custom software that addresses their specific pain points and helps them achieve their goals.

Whether you're in the construction industry, real estate, urban planning, or any other sector, Mthoe Saps Construction Technologies can help you unlock the power of your data and streamline your workflows. Contact us today to learn more about how we can help your business thrive.
    """)

# Render the selected page
if selection == "Home🏠":
    home_page()
#else:
    #enquiry_page()

if selection == "FAQ(s)/ About us❓":
    about_page()


if selection == "Enquiry📩":
    enquiry_page()
    