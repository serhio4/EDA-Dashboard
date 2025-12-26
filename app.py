import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Dashboard EDA' ,layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('imdb_top_1000.csv')

    df['Gross'] = df['Gross'].str.replace(',', '').astype(float)
    df['Runtime'] = (df['Runtime'].str.replace(' min', '', regex=False).pipe(pd.to_numeric, errors='coerce'))
    df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')

    return df

df = load_data()


st.sidebar.header('Filtre')

all_genres = set(', '.join(df['Genre'].unique()).replace(', ', ',').split(','))
selected_genres = st.sidebar.multiselect('Alege genul', sorted(list(all_genres)))

min_year = int(df['Released_Year'].min())
max_year = int(df['Released_Year'].max())
year_range = st.sidebar.slider('Interval Anul Lansarii', min_year, max_year, (1990, 2020))

min_rating = st.sidebar.slider('Rating IMDb Minim', 7.0, 10.0, 8.0, step=0.1)

filtered_df = df.copy()

filtered_df = filtered_df[
    (filtered_df['Released_Year'] >= year_range[0]) &
    (filtered_df['Released_Year'] <= year_range[1])
]

filtered_df = filtered_df[filtered_df['IMDB_Rating'] >= min_rating]

if selected_genres:
    mask = filtered_df['Genre'].apply(lambda x: any(genre in x for genre in selected_genres))
    filtered_df = filtered_df[mask]

st.title('Top 1000 IMDb')
st.markdown(f'Analizam **{len(filtered_df)}** filme pe baza filtrelor tale.')

col1, col2, col3 = st.columns(3)
col1.metric("Rating Mediu", round(filtered_df['IMDB_Rating'].mean(), 2))
mean_runtime = filtered_df['Runtime'].mean()

if pd.notna(mean_runtime):
    col2.metric("Durata Medie", f"{int(mean_runtime)} min")
else:
    col2.metric("Durata Medie", "N/A")


total_gross = filtered_df['Gross'].sum()

if total_gross > 1_000_000_000:
    col3.metric('Incasari totale', f'${total_gross / 1_000_000_000:.2f} B')
else:
    col3.metric('Incasari totale', f'${total_gross / 1_000_000:.2f} M')

tab1, tab2, tab3 = st.tabs(['Grafice', 'Date Brute', 'Postere'])
with tab1:
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Top 10 Filme (după Rating)")

        top_10 = filtered_df.sort_values(by="IMDB_Rating", ascending=False).head(10)
        fig_bar = px.bar(
            top_10,
            x="IMDB_Rating",
            y="Series_Title",
            orientation='h',
            title="Top 10 Filme Filtrate",
            color="IMDB_Rating",
            color_continuous_scale="Viridis"
        )

        fig_bar.update_layout(yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig_bar, use_container_width=True)

    with c2:
        st.subheader('Rating vs Incasari')
        fig_scatter = px.scatter(
            filtered_df,
            x='IMDB_Rating',
            y='Gross',
            size='No_of_Votes',
            color='Genre',
            hover_name='Series_Title',
            title='Relatia dintre Calitate si Bani',
            log_y=True
        )

        st.plotly_chart(fig_scatter, use_container_width=True)

with tab2:
    st.dataframe(filtered_df)

with tab3:
    st.subheader('Postere pentru primele 5 filme selectate')
    cols = st.columns(5)

    top_posters = filtered_df.head(5)
    for index, (i, row) in enumerate(top_posters.iterrows()):
        with cols[index]:
            st.image(row['Poster_Link'], caption=row['Series_Title'])
            st.write(f'⭐ {row['IMDB_Rating']}')













