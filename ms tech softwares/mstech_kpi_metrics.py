import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
from datetime import datetime, timedelta
from PIL import Image

# Set page title and favicon
st.set_page_config(page_title="Mthoe Saps Construction Technologies", page_icon="📈", initial_sidebar_state="expanded")

col1, col2 = st.columns(2)
with col1:
    st.title("Mthoe Saps Construction Technologies Metric Analysis Platform")
with col2:
    image = Image.open("ms tech softwares/vids and img/logo3.png")
    st.image(image, use_column_width=False, width=250, caption="Welcome to our Stakeholders Company Metric Analysis Platform")

# Define the KPI metrics
data = {
    "📈 Annual Recurring Revenue (ARR)": 64699.80,
    "📊 Monthly Recurring Revenue (MRR)": 5391.65,
    "💰 Customer Lifetime Value (LTV)": 33680,
    "💸 Average Revenue Per User (ARPU)": 4201.29,
    "🏆 Gross Margin": 0.8,
    "📉 Churn Rate": 0.1,
    "📈 Share Price": 0.50
}

# Create the Streamlit tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["KPIs and Calculators", "Company forecasts", "SaaS Companies Overseas", "World Internet Usage", "World Economic Perfomance"])

with tab1:
    with st.container(border=True):
        st.subheader("Company Analysis Metric Dashboard", divider=True)
    # Display the KPI metrics and input fields in an expander
    with st.expander("💰 Revenue and Monetization KPIs"):
        for metric, value in data.items():
            if metric in ["🏆 Gross Margin", "📉 Churn Rate"]:
                value_str = "{:.0%}".format(value)
            elif metric == "📈 Share Price":
                value_str = "${:,.2f}".format(value)
            else:
                value_str = "${:,.2f}".format(value)
            st.markdown(f"<div style='border: 2px solid #007bff; padding: 10px; border-radius: 5px;'>{metric}: {value_str}</div>", unsafe_allow_html=True)

    # Add input field and display the calculated results
    with st.expander("Investment Calculator"):
        investment_amount = st.slider("Enter investment amount:", min_value=0.0, max_value=3500.00, step=0.01)
        share_price = data["📈 Share Price"]
        shares_received = investment_amount / share_price
        st.write(f"At an investment of ${investment_amount:,.2f}, you would receive {shares_received:.2f} shares.")

    # Land area management
    def land_area_management():
        with st.container(border=True):
            st.subheader("Bulawayo Data Land Management Indicator", divider=True)
            st.write("""This indicator shows our dataset that has a meshed geolocation indicator
                     that highlights all the Suburbs of Bulawayo, we can simulate any mapping system
                     showing our ability to manage any system.""")
        # Load data from a CSV file or GeoJSON file
        data = pd.read_excel('ms tech softwares/databases/bulawayo_map_coordinates.xlsx')

        fig = px.scatter_mapbox(data, lat="latitude", lon="longitude", hover_name="suburb",
                               color_discrete_sequence=["fuchsia"], zoom=10, height=500)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        st.plotly_chart(fig, use_container_width=True)

        with st.container(border=True):
            st.subheader("World Data Management Indicator", divider=True)
            st.write("""This indicator shows our dataset that has a meshed geolocation indicator
                     that highlights all the Countries of the world, we can simulate any mapping system
                     showing our ability to manage any system.""")
        
        # Load the GDP data for each country
        gdp_data = {
    'AFG': 20.22, 'AGO': 93.21, 'ALB': 15.06, 'ARE': 354.25, 'ARG': 384.17, 'ARM': 13.38,
    'ATA': 0.0, 'ATF': 0.0, 'AUS': 1369.55, 'AUT': 435.13, 'AZE': 47.76, 'BDI': 3.07,
    'BEL': 484.62, 'BEN': 10.36, 'BFA': 13.69, 'BGD': 274.02, 'BGR': 55.16, 'BHS': 11.96,
    'BIH': 18.55, 'BLR': 54.49, 'BLZ': 1.85, 'BOL': 37.51, 'BRA': 1839.76, 'BRN': 12.14,
    'BTN': 2.35, 'BWA': 17.15, 'CAF': 2.07, 'CAN': 1711.4, 'CHE': 703.13, 'CHL': 277.07,
    'CHN': 14342.9, 'CIV': 36.17, 'CMR': 37.92, 'COD': 47.32, 'COG': 11.81, 'COL': 271.37,
    'CRI': 57.06, 'CUB': 100.02, 'CYP': 21.76, 'CZE': 245.81, 'DEU': 3845.63, 'DJI': 2.39,
    'DNK': 335.66, 'DOM': 78.82, 'DZA': 169.98, 'ECU': 98.1, 'EGY': 302.24, 'ERI': 2.77,
    'ESP': 1245.53, 'EST': 30.26, 'ETH': 93.97, 'FIN': 268.39, 'FJI': 5.42, 'FRA': 2582.5,
    'FRO': 2.41, 'GAB': 14.85, 'GBR': 2640.42, 'GEO': 15.87, 'GHA': 66.98, 'GIN': 12.11,
    'GMB': 1.67, 'GNB': 1.12, 'GNQ': 10.18, 'GRC': 187.44, 'GRL': 2.21, 'GTM': 77.67,
    'GUY': 5.18, 'HND': 23.81, 'HRV': 55.06, 'HTI': 8.72, 'HUN': 155.72, 'IDN': 1058.42,
    'IND': 2709.44, 'IRL': 398.92, 'IRN': 591.01, 'IRQ': 170.51, 'ISL': 21.9, 'ISR': 394.59,
    'ITA': 1886.45, 'JAM': 15.8, 'JOR': 40.66, 'JPN': 4910.56, 'KAZ': 169.46, 'KEN': 95.51,
    'KGZ': 7.61, 'KHM': 27.01, 'KOR': 1619.43, 'KWT': 114.56, 'LAO': 18.13, 'LBN': 55.77,
    'LBR': 3.06, 'LBY': 25.12, 'LCA': 1.74, 'LKA': 84.01, 'LSO': 2.36, 'LTU': 54.38,
    'LUX': 73.72, 'LVA': 34.8, 'MAR': 114.74, 'MDA': 12.56, 'MDG': 10.81, 'MEX': 1221.61,
    'MKD': 12.57, 'MLI': 17.42, 'MMR': 71.21, 'MNE': 5.56, 'MNG': 13.11, 'MOZ': 14.85,
    'MRT': 5.33, 'MWI': 6.75, 'MYS': 336.99, 'NAM': 10.73, 'NCL': 9.91, 'NER': 8.06,
    'NGA': 448.12, 'NIC': 12.2, 'NLD': 880.69, 'NOR': 398.83, 'NPL': 30.56, 'NZL': 205.97,
    'OMN': 77.07, 'PAK': 263.39, 'PAN': 55.17, 'PER': 211.39, 'PHL': 334.06, 'PNG': 21.45,
    'POL': 594.24, 'PRI': 103.09, 'PRK': 16.51, 'PRT': 219.74, 'PRY': 27.98, 'QAT': 167.61,
    'ROU': 199.95, 'RUS': 1647.47, 'RWA': 10.12, 'ESH': 0.0, 'SAU': 793.51, 'SDN': 37.75,
    'SEN': 23.88, 'SLB': 1.27, 'SLE': 3.92, 'SLV': 26.21, 'SOM': 4.7, 'SRB': 51.51,
    'SSD': 5.26, 'SUR': 3.42, 'SVK': 103.57, 'SVN': 54.25, 'SWE': 531.08, 'SWZ': 4.37,
    'SYR': 2.45, 'TCD': 10.7, 'TGO': 6.13, 'THA': 505.99, 'TJK': 7.8, 'TKM': 40.31,
    'TLS': 2.58, 'TON': 0.48, 'TTO': 21.58, 'TUN': 38.78, 'TUR': 761.43, 'TWN': 589.52,
    'TZA': 61.03, 'UGA': 27.73, 'UKR': 150.18, 'URY': 55.98, 'USA': 21427.6, 'UZB': 57.74,
    'VEN': 96.92, 'VNM': 261.92, 'VUT': 0.85, 'WSM': 0.75, 'YEM': 26.77, 'ZAF': 358.84,
    'ZMB': 21.19, 'ZWE': 21.45
        }

        # Load the Plotly built-in world map dataset
        world_map = go.Figure(data=go.Choropleth(
            locations=list(gdp_data.keys()),
            z=list(gdp_data.values()),
            colorscale='Viridis',
            reversescale=True,
            #hover_data="GDP (in billions USD)",
            #hover_name="country",
            marker_line_color='darkgrey',
            marker_line_width=0.5,
            colorbar_title='GDP (in billions USD)'
        ))

        world_map.update_layout(
            title_text='World Map by GDP',
            geo=dict(
                showframe=False,
                showcoastlines=False,
                projection_type='equirectangular'
            )
        )


        st.plotly_chart(world_map, use_container_width=True)

    with st.expander("Land Area Management Perfomance Indicator"):
        land_area_management()
    st.divider()
    st.write("This platform showcases the key performance indicators (KPIs) for Mthoe Saps Construction Technologies, a technovative land development SaaS company.")

with tab2:
    # Company metrics
    def get_share_price(slide_date):
        return 0.50 * (1 + (slide_date - 2024) * 0.1576)

    def get_total_company_value(slide_date):
        return 20000 * (1 + (slide_date - 2024) * 0.1576)

    shares_outstanding = 40000

    # Calculate 1% of company value
    def calculate_one_percent_value(slide_date):
        return 0.01 * get_total_company_value(slide_date)

    # Calculate number of shares for 1% of company
    def calculate_shares_for_one_percent(slide_date):
        return calculate_one_percent_value(slide_date) / get_share_price(slide_date)

    # Calculate forecasted shares
    def calculate_forecasted_shares(slide_date):
        return shares_outstanding * (1 + (slide_date - 2024) * 0.1576)

    # Calculate delta
    def calculate_delta(slide_date):
        forecasted_shares = calculate_forecasted_shares(slide_date)
        return forecasted_shares - shares_outstanding

    with st.container(border=True):
        # Display the metrics
        st.subheader("Company Future Forecast Metrics Dashboard", divider=True)
        st.write("Exponential Growth of company estimated to be at 15.76% annually")

    # Slider for forecasted date
    slide_date = st.slider("Forecast Date", min_value=2024, max_value=2030, value=2024, step=1)

    # Create a dataframe for the line chart
    years = list(range(2024, 2031))
    share_prices = [get_share_price(year) for year in years]
    company_values = [get_total_company_value(year) for year in years]
    forecasted_shares = [calculate_forecasted_shares(year) for year in years]
    shares_for_one_percent = [calculate_shares_for_one_percent(year) for year in years]
    df = pd.DataFrame({
        "Year": years,
        "Share Price": share_prices,
        "Company Value": company_values,
        "Forecasted Shares": forecasted_shares,
        "Shares for 1% of Company": shares_for_one_percent
    })

    # Create the line chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Year"], y=df["Share Price"], mode="lines+markers", name="Share Price"))
    fig.add_trace(go.Scatter(x=df["Year"], y=df["Company Value"], mode="lines+markers", name="Company Value"))
    fig.add_trace(go.Scatter(x=df["Year"], y=df["Forecasted Shares"], mode="lines+markers", name="Forecasted Shares"))
    fig.add_trace(go.Scatter(x=df["Year"], y=df["Shares for 1% of Company"], mode="lines+markers", name="Shares for 1% of Company"))
    fig.update_layout(
        title="Company Metrics Over Time",
        xaxis_title="Year",
        yaxis_title="Value",
        hovermode="x unified"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Share Price", value=f"${get_share_price(slide_date):.2f}")
        st.metric(label="Shares Outstanding", value=f"{shares_outstanding:,}")
        st.metric(label="Forecasted Shares", value=f"{calculate_forecasted_shares(slide_date):,.0f}", delta=f"{calculate_delta(slide_date):,.0f}")

    with col2:
        st.metric(label="Total Company Value", value=f"${get_total_company_value(slide_date):,.0f}")
        st.metric(label="Shares for 1% of Company", value=f"{calculate_shares_for_one_percent(slide_date):,.0f}")
        st.metric(label="1% of Company Value", value=f"${calculate_one_percent_value(slide_date):,.0f}")
    st.divider()
    # Display the line chart
   # st.plotly_chart(fig, use_container_width=True)

    # Add interaction and annotations
    st.write("**Hover over the chart to see the values for each year.**")
    selected_year = st.selectbox("Select a year to highlight:", df["Year"])
    fig.add_vline(x=selected_year, line_width=2, line_dash="dash", line_color="red")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    with st.container(border=True):
        st.subheader("SaaS KPI Metric Analysis", divider=True)
        st.info("Data Hut ycombinator startups datasets")
        st.write("Dataset based on US SaaS startup companies")

    df = pd.read_csv('ms tech softwares/databases/data-hut-ycombinator-startups/data/yc_sample.csv')

    with st.expander("Pie Chart"):
        # Pie Chart
        fig = px.pie(df, values="team_size", 
                     labels="founded_year", 
                     hover_name="company_name",
                     hover_data="tagline",
                     color=None,
                     title="Pie Chart showing company and their services/product provision")
        st.plotly_chart(fig)

    with st.expander("Bar Chart - Team Size by Founded Year"):
        # Bar Chart
        fig = px.bar(df, x="company_name", y="number_of_founders", 
                     hover_name="country",
                     hover_data="founded_year",
                     color="company_type",
                     title="Bar Chart showing Team Size by Founded Year")
        st.plotly_chart(fig)

    with st.expander("Bar Chart - Team Size by Country"):
        # Bar Chart
        fig = px.bar(df, x="country", y="team_size", 
                     hover_name="company_name",
                     hover_data="tagline",
                     color="company_type",
                     title="Bar Chart showing Team Size by Country")
        st.plotly_chart(fig)

    with st.expander("Scatter Plot - Team Size by Founded Year and Industry Tags"):
        # Scatter Plot
        fig = px.scatter(df, x="founded_year", y="team_size",
                         hover_name="company_name",
                         hover_data="tagline",
                         #color="industry_tags",
                         title="Scatter Plot showing Team Size by Founded Year and Industry Tags")
        st.plotly_chart(fig)

    with st.expander("Histogram - Team Size"):
        # Histogram
        fig = px.histogram(df, x="team_size", 
                           nbins=20,
                           color="company_type",
                           hover_name="company_name",
                           hover_data="country",
                           title="Histogram of Team Sizes")
        st.plotly_chart(fig)

with tab4:
    with st.container(border=True):
        st.subheader("Internet Usage Dataset Analysis", divider=True)

    df = pd.read_csv("ms tech softwares/databases/garyhoov-world-bank-data/data/countries_in_alpha_order.csv")
    #st.dataframe(df.tail())

    # Add filters
    country_filter = st.multiselect("Select countries", df["country_name"].unique())
    population_total_filter = st.slider("Filter by Population Total", 
                                       int(df["population_total"].min()), 
                                       int(df["population_total"].max()),
                                       (int(df["population_total"].min()), int(df["population_total"].max())))
    internet_users_filter = st.slider("Filter by Internet Users per 100 People",
                                     float(df["internet_users_per_100_people"].min()),
                                     float(df["internet_users_per_100_people"].max()),
                                     (float(df["internet_users_per_100_people"].min()), 
                                      float(df["internet_users_per_100_people"].max())))

    # Apply the filters
    if country_filter:
        df = df[df["country_name"].isin(country_filter)]
    df = df[(df["population_total"] >= population_total_filter[0]) & (df["population_total"] <= population_total_filter[1])]
    df = df[(df["internet_users_per_100_people"] >= internet_users_filter[0]) & (df["internet_users_per_100_people"] <= internet_users_filter[1])]

    fig = px.bar(df,
                  x="country_name",
                  y="internet_users_per_100_people",
                  color="population_cgr_1960_2015",
                  hover_name="country_code",
                  hover_data=["population_total"])
    st.plotly_chart(fig)
    st.divider()
   
    with st.container(border=True):
        st.subheader("New York Times Dataset of Country Articles Mention Times", divider=True)

    # Specify the Excel file path
    file_path = 'ms tech softwares/databases/ansakoy-countries-in-new-york-times-2000-2016/data/ny_times_countries_2000_2016.csv'

    # Load the Excel data into a Pandas DataFrame
    df = pd.read_csv(file_path)

    # Add filters
    start_year = st.number_input("Start Year", min_value=2000, max_value=2016, value=2000, step=1)
    end_year = st.number_input("End Year", min_value=2000, max_value=2016, value=2016, step=1)
    df = df[(df["year"] >= start_year) & (df["year"] <= end_year)]

    country_filter = st.multiselect("Select countries", df["country"].unique())
    if country_filter:
        df = df[df["country"].isin(country_filter)]

    # Display the filtered data in a Streamlit table
    #st.dataframe(country_filter)

    fig = px.bar(df,
                  x="country",
                  y="num_occurrences",
                  color="year",
                  hover_name="country",
                  hover_data="num_occurrences")
    st.plotly_chart(fig)

with tab5:
    with st.container(border=True):
        st.subheader("World Data KPIs for MS Tech Market Research", divider=True)

    country_data = px.data.gapminder()
    #st.dataframe(country_data.tail())

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.subheader("Filter by Continent", divider=True)
            #st.write("Select Continent to start Analysis")
            selected_continent = st.multiselect("Select Continent(s)", country_data['continent'].unique())
            filtered_data = country_data[country_data['continent'].isin(selected_continent)]

    with col2:
        with st.container(border=True):
            st.subheader("Filter by GDP per Capita", divider=True)
            min_gdp = country_data['gdpPercap'].min()
            max_gdp = country_data['gdpPercap'].max()
            gdp_range = st.slider("Select GDP per Capita Range", min_value=min_gdp, max_value=max_gdp, value=(min_gdp, max_gdp), step=1000.0)
            filtered_data = filtered_data[(filtered_data['gdpPercap'] >= gdp_range[0]) & (filtered_data['gdpPercap'] <= gdp_range[1])]

    with col3:
        with st.container(border=True):
            st.subheader("Filter by Population", divider=True)
            min_pop = country_data['pop'].min()
            max_pop = country_data['pop'].max()
            pop_range = st.slider("Select Population Range", min_value=min_pop, max_value=max_pop, value=(min_pop, max_pop), step=1000000)
            filtered_data = filtered_data[(filtered_data['pop'] >= pop_range[0]) & (filtered_data['pop'] <= pop_range[1])]
    st.divider()
    #st.text("Select Continent to start Analysis")

    fig2 = px.area(filtered_data,
                  x="country",
                  y="pop",
                  hover_name="continent",
                  hover_data="gdpPercap",
                  )
    st.plotly_chart(fig2)

    fig3 = px.area(filtered_data,
                  x="country",
                  y="gdpPercap",
                  hover_name="continent",
                  hover_data="country",
                  )
    st.plotly_chart(fig3)

def faq_section():
    st.sidebar.title("FAQs 💬")

    with st.sidebar.expander("General Questions"):
        st.write("**What is the Mthoe Saps Construction Technologies SaaS? 🏢**")
        st.write("The Mthoe Saps Construction Technologies SaaS is a comprehensive platform that provides KPI metric analysis and research for land development projects.")
        st.write("**Who is the target audience? 👨‍💼👩‍💼**")
        st.write("The primary target audience includes real estate developers, land planners, and municipal authorities involved in land development projects.")

    with st.sidebar.expander("Features and Functionalities"):
        st.write("**What are the key features of the SaaS? 🔍**")
        st.checkbox("KPI Metric Analysis", value=True)
        st.checkbox("Customizable Dashboards", value=True)
        st.checkbox("Predictive Analytics", value=True)
        st.checkbox("Collaboration and Sharing", value=False)

    with st.sidebar.expander("Pricing and Plans"):
        st.write("**What are the pricing options? 💰**")
        st.write("We offer a variety of industry related services, head over to our main website and head over to the enquiries page to send an enquiry form for your business.")
        st.link_button("MS Tech Main website", "https://www.example.com")#__replace this link with a real one
        plan = st.radio("Plans Include:", ["Free 🆓", "Basic 🟢", "Pro 🟠", "Enterprise 🔴"])
        if plan == "Free 🆓":
            st.write("The free plan includes limited access to KPI metrics and analysis.")
        elif plan == "Basic 🟢":
            st.write("The basic plan includes access to core KPI metrics and analysis tools.")
        elif plan == "Pro 🟠":
            st.write("The pro plan includes advanced KPI metrics, predictive analytics, and custom dashboard features.")
        else:
            st.write("The enterprise plan offers a comprehensive suite of features, dedicated support, and enterprise-level security.")

    with st.sidebar.expander("Contact Us 📞"):
        st.write("**Have any questions or feedback? 💡**")
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
def contact_us():
    st.write("Thank you for your interest! Our team will be in touch with you shortly. 🙌")

faq_section()