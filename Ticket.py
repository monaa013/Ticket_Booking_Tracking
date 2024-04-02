import streamlit as st 
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Travello",
    page_icon="🚌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dashboard 1: Home Page
def home_page():
    st.title('🚌 Welcome to Travello! 🌍')
    st.subheader('Your Ultimate Ticket Booking and Tracking Experience')

    # Fun intro
    st.write('🎉 Ready to embark on an adventure? Look no further!')

    st.write('🚌 Hop aboard the Travello express, where your journey begins with just a click!')

    st.write('💼 Whether you\'re planning a weekend getaway or a cross-country excursion, Travello has got you covered!')

    # Display images side by side vertically
    st.write("### Get ready to explore with these amazing rides! 🚗🚌🚐")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("van.jpeg", caption="Bus - Your Comfortable Ride", use_column_width=True)

    with col2:
        st.image("duck.jpeg", caption="Van - Adventure Awaits!", use_column_width=True)

    with col3:
        st.image("panda.jpeg", caption="Car - Freedom on Wheels", use_column_width=True)

# Dashboard 2: Vehicle Category Selection
def vehicle_category():
    st.title('🚌 Vehicle Category Selection')
    st.write('Please select your preferred vehicle category:')
    
    # Vehicle categories dropdown
    selected_vehicle_category = st.selectbox('Select Vehicle Category', ['Car🚗', 'Van🚐', 'Bus🚌', 'Mini Bus🚐'])

    if selected_vehicle_category == 'Car🚗':
        st.subheader('Car Details🚗')
        # Number of seats slider
        num_seats = st.slider('Number of Seats 💺', min_value=2, max_value=7, value=5)
        st.write(f'Number of Seats: {num_seats}')
        
        # AC/Non-AC option
        ac_option = st.radio('AC/Non-AC ❄️/🔥', ['AC ❄️', 'Non-AC 🔥'])
        st.write(f'AC/Non-AC: {ac_option}')

        # Fuel type dropdown
        fuel_type = st.selectbox('Fuel Type ⛽', ['Petrol', 'Diesel', 'Electric'])
        st.write(f'Fuel Type: {fuel_type}')
        
        st.write('Availability: Available')
        st.write('Price: $2000 per hour 💰')
    elif selected_vehicle_category == 'Van🚐':
        st.subheader('Van Details🚐')
        # Number of seats slider
        num_seats = st.slider('Number of Seats 💺', min_value=5, max_value=15, value=8)
        st.write(f'Number of Seats: {num_seats}')

        # AC/Non-AC option
        ac_option = st.radio('AC/Non-AC ❄️/🔥', ['AC ❄️', 'Non-AC 🔥'])
        st.write(f'AC/Non-AC: {ac_option}')

        # Fuel type dropdown
        fuel_type = st.selectbox('Fuel Type ⛽', ['Petrol', 'Diesel', 'Electric'])
        st.write(f'Fuel Type: {fuel_type}')

        st.write('Availability: Available')
        st.write('Price: $2500 per hour 💰')
    elif selected_vehicle_category == 'Bus🚌':
        st.subheader('Bus Details🚌')
        # Number of seats slider
        num_seats = st.slider('Number of Seats 💺', min_value=20, max_value=50, value=30)
        st.write(f'Number of Seats: {num_seats}')

        # AC/Non-AC option
        ac_option = st.radio('AC/Non-AC ❄️/🔥', ['AC ❄️', 'Non-AC 🔥'])
        st.write(f'AC/Non-AC: {ac_option}')

        # Fuel type dropdown
        fuel_type = st.selectbox('Fuel Type ⛽', ['Diesel', 'Electric'])
        st.write(f'Fuel Type: {fuel_type}')

        st.write('Availability: Available')
        st.write('Price: $5000 per hour 💰')
    elif selected_vehicle_category == 'Mini Bus🚐':
        st.subheader('Mini Bus Details🚐')
        # Number of seats slider
        num_seats = st.slider('Number of Seats 💺', min_value=10, max_value=25, value=20)
        st.write(f'Number of Seats: {num_seats}')

        # AC/Non-AC option
        ac_option = st.radio('AC/Non-AC ❄️/🔥', ['AC ❄️', 'Non-AC 🔥'])
        st.write(f'AC/Non-AC: {ac_option}')

        # Fuel type dropdown
        fuel_type = st.selectbox('Fuel Type ⛽', ['Petrol', 'Diesel', 'Electric'])
        st.write(f'Fuel Type: {fuel_type}')

        st.write('Availability: Available')
        st.write('Price: $4000 per hour 💰')

    if st.button('Submit'):
        st.success('Submitted successfully!')

# Dashboard 3: Booking Form
def booking_form():
    st.title('🎫Ticket Booking Form')
    st.write('Please fill out the following details to book your ticket:')
    
    # Form fields
    name = st.text_input('Name')
    age = st.number_input('Age', min_value=1, max_value=120)
    gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
    mobile_number = st.text_input('Mobile Number')
    mail_id = st.text_input('Mail id')
    from_location = st.text_input('From Location')
    drop_location = st.text_input('Drop Location')
    start_timing = st.time_input('Start Timing')
    drop_timing = st.time_input('Drop Timing')
    starting_date = st.date_input('Starting Date (Departure Date)')
    returning_date_option = st.checkbox('Return Journey')
    returning_date = None
    if returning_date_option:
        returning_date = st.date_input('Returning Date (Departure Date)')

    # Add Passenger option
    add_passenger = st.checkbox('Add Passenger')

    # Additional Passenger fields
    if add_passenger:
        st.subheader('Passenger Details:')
        passenger_name = st.text_input('Passenger Name')
        passenger_age = st.number_input('Passenger Age', min_value=1, max_value=120)
        passenger_gender = st.selectbox('Passenger Gender', ['Male', 'Female', 'Other'])
    
    # Submit button
    if st.button('Book Ticket'):
        # Process booking logic here
        ticket_details = {
            'Name': name,
            'Age': age,
            'Gender': gender,
            'Mobile Number': mobile_number,
            'Mail id': mail_id,
            'From Location': from_location,
            'Drop Location': drop_location,
            'Start Timing': start_timing,
            'Drop Timing': drop_timing,
            'Starting Date': starting_date,
            'Returning Date': returning_date if returning_date_option else None
        }
        booked_tickets = st.session_state.get('booked_tickets', [])
        booked_tickets.append(ticket_details)
        st.session_state.booked_tickets = booked_tickets
        st.success('Ticket booked successfully!')

# Dashboard 4: Ticket Tracking
def ticket_tracking():
    st.title('📍Ticket Tracking')
    st.write('Track your booked tickets here.')

    # Display ticket tracking information
    booked_tickets = st.session_state.get('booked_tickets', [])

    if not booked_tickets:
        st.write('No tickets booked yet.')
    else:
        st.write('Your booked tickets:')
        for i, ticket in enumerate(booked_tickets, start=1):
            st.write(f"**Ticket {i} Details**")
            
            # Display date, time, and starting location vertically with dropdown menu
            st.write('**Date:**', ticket['Starting Date'])
            st.write('**Time:**', ticket['Start Timing'])
            st.write('**Starting Location:**', ticket['From Location'])
            
            # Add dropdown menu for additional details
            st.write('---')  # Separator
            st.write('**More Options:**')
            with st.expander('View Additional Details'):
                st.write(f"**Name:** {ticket['Name']}")
                st.write(f"**Age:** {ticket['Age']}")
                st.write(f"**Gender:** {ticket['Gender']}")
                st.write(f"**Mobile Number:** {ticket['Mobile Number']}")
                st.write(f"**Mail id:** {ticket['Mail id']}")

# Dashboard 5: About Page
def about_page():
    st.title('About 🚌 Travello!')
    st.write('Travello is India\'s largest brand for online bus ticket booking and offers an easy-to-use online bus ticket booking service and train, With over 36 million satisfied customers, 3500+ bus operators to choose from, and plenty of offers on bus ticket booking, Travello makes road journeys super convenient for travelers. A leading platform for booking bus tickets, redBus has been the leader in online bus booking over the past 17 years across thousands of cities and lakhs of routes in India.')
    st.write('Booking a bus ticket online on redBus app or website is very simple. You can download the redBus app or visit redbus.in and enter your source, destination & travel date to check the top-rated bus services available. You can then compare bus prices, user ratings & bus amenities, select your preferred seat, boarding & dropping points and make the payment using multiple payment options like UPI, debit or credit card, net banking and more. With redBus get assured safe & secure payment methods and guaranteed travel with the best seat and bus operator of your choice. Once the bus booking payment is confirmed, all you have to do is pack your bags and get ready to travel with the m-ticket which you can show to the bus operator on your mobile before boarding the bus. Online bus ticket booking with Travello is that simple!')
    st.write('Travello also offers other exclusive benefits on online bus tickets like flexible ticket reschedule options, easy & friendly cancellation policies, instant payment refund. With live bus tracking feature, you can plan your travel and never miss the bus. You can get the cheapest bus tickets by availing the best discounts for new & existing customers. With redDeals, you can also get exclusive & additional discounts on your online bus ticket booking. You will get 24X7 customer support on call, chat & help to resolve all your queries in English & local languages.')
    st.write('Travello offers Primo bus services which are specially curated by redBus with highly-rated buses with best-in-class service. With Primo by Travello, you can be assured of safe, comfortable & on-time bus service at no additional cost. With multiple boarding & dropping points available across all major cities in India, you can select as per your convenience and enjoy a smooth travel experience.')
    st.write('Travello operates in 6 countries including India, Malaysia, Singapore, Indonesia, Peru, and Colombia and has sold over 220 million bus tickets worldwide through the Travello website and app. With over 36 million satisfied customers. Travello is committed to providing a world-class online bus booking experience to its users.')
    st.write('Travello offers bus tickets from some of the top private bus operators like Orange Travels, VRL Travels, SRS Travels, Chartered Bus, Praveen Travels and state government bus operators like APSRTC, TSRTC, MSRTC, GSRTC, Kerala RTC, TNSTC, RSRTC, UPSRTC, KSRTC Karnataka and more. With redBus, customers have the flexibility of booking bus tickets of different bus types like AC/non-AC, Sleeper, Seater, Volvo, Multi-axle, AC Sleeper, Electric buses and more.')
    st.write('For any queries, please contact us at xyz@example.com')

# Dashboard 6: Plotting
def plotting():
    st.title('📊 Journey through Opinions: Unveiling Perceptions of the Free Bus Scheme')
    st.subheader('Survey Data Analysis: Exploring Public Perception of Free Bus Service')
    st.write('In this analysis, we delve into survey data collected from individuals to understand their perceptions and experiences with a free bus service initiative. The dataset encompasses various demographic attributes and responses to survey questions related to the utilization and impact of the free bus service. As we journey through the data, we aim to uncover insights that shed light on the effectiveness and reception of the initiative, providing valuable insights for policymakers and transportation authorities.Now, let\'s embark on our exploration and visualize the survey findings through an array of informative plots.')
    st.write('Visualize the survey data with different plots.')

    # Load data
    @st.cache_data
    def load_data():
        return pd.read_csv("bus.csv")

    data = load_data()

    # Replace missing values
    data.fillna({'Mail ID': 'Not provided', 'Where do you reside?': 'Not provided'}, inplace=True)

    # Sidebar - Plot options
    st.sidebar.title("Plot Options")
    plot_options = ['Line Plot', 'Box Plot', 'Scatter Plot', 'Histogram', 'Violin Plot']
    selected_plot = st.sidebar.selectbox("Select Plot Type", plot_options)

    # Plotting selected plot
    if selected_plot == 'Line Plot':
        st.subheader("Line Plot")
        fig = px.line(data, x='Timestamp', y='Age', title='Age Trend Over Time')
        st.plotly_chart(fig)
    elif selected_plot == 'Box Plot':
        st.subheader("Box Plot")
        fig = px.box(data, y='Age', title='Age Distribution')
        st.plotly_chart(fig)
    elif selected_plot == 'Scatter Plot':
        st.subheader("Scatter Plot")
        fig = px.scatter(data, x='Age', y='Occupation', title='Age vs Occupation')
        st.plotly_chart(fig)
    elif selected_plot == 'Histogram':
        st.subheader("Histogram")
        fig = px.histogram(data, x='Age', title='Age Distribution')
        st.plotly_chart(fig)
    elif selected_plot == 'Violin Plot':
        st.subheader("Violin Plot")
        fig = px.violin(data, y='Age', title='Age Distribution')
        st.plotly_chart(fig)

# Main function to control navigation between dashboards
def main():
    st.sidebar.title('Travello')
    selected_page = st.sidebar.radio('Go to', ['Home', 'Vehicle', 'Booking Form', 'Ticket Tracking', 'About', 'Wanna Know?!'])

    if selected_page == 'Home':
        home_page()
    elif selected_page == 'Vehicle':
        vehicle_category()  
    elif selected_page == 'Booking Form':
        booking_form()
    elif selected_page == 'Ticket Tracking':
        ticket_tracking()
    elif selected_page == 'About':
        about_page()
    elif selected_page == 'Wanna Know?!':
        plotting()

if __name__ == '__main__':
    main()
