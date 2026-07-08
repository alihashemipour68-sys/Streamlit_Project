import streamlit as st
import Final_Func_db
import Final_Creat_db
import app_api_list0


st.title('Search Film According to Your Idea')

option=st.sidebar.selectbox('Enter your option',('Add Movie Manually','Add Movie From API','Movie Info By Name','Movie Info By IMDB',\
                                                 'Movie Info By Year Building','Sort Movie By Oscar Nominated',\
                                                'Sort Movie By Oscar Won',\
                                                'Movie Info By Country','Delete film','Edit Film','Restore Default'))
                                                                                                                                                
def get_country_emoji(country_name):
    country_emojis = {
        'Iran': '🇮🇷',
        'USA': '🇺🇸',
        'America': '🇺🇸',
        'England': '🇬🇧',
        'UK': '🇬🇧',
        'France': '🇫🇷',
        'Germany': '🇩🇪',
        'Italy': '🇮🇹',
        'Spain': '🇪🇸',
        'Japan': '🇯🇵',
        'India': '🇮🇳',
        'Ukraine': '🇺🇦',
    }
    
    for key, emoji in country_emojis.items():
        if key in country_name:
            return emoji
    return '🌎'

def Film_Result_Display(result, search_word=None):
    for i in range(len(result)):
        title = result[i][1]
    
        if search_word:
            word_lower = search_word.lower()
            title_lower = title.lower()
            
            if word_lower in title_lower:
                start = title_lower.find(word_lower)
                end = start + len(search_word)
                
                before = title[:start]
                word = title[start:end]
                after = title[end:]
                
                title = f"{before}:red[{word}]{after}"
        
        st.write(f"{result[i][0]}-🎬 Title: {title},\
                  ⭐ IMDB: {result[i][2]}/10,\
                  📅 Year: {result[i][3]}, \
                  🌍 Country: {result[i][4]} {get_country_emoji(result[i][4])},\
                  🏆 Awards: {result[i][5]}, \
                  🎭 Genres: {result[i][6]}")
        st.write(f"📖 Plot: {result[i][7]}")
        st.image(f'{result[i][8]}')
              
if option =='Add Movie Manually':
    Film_Name=st.text_input('Please Enter movie name ')
    imdb=st.number_input('Enter IMDB Rating ',min_value=5.0,max_value=10.0,step=0.1)
    if st.button('Insert Movie'):
                st.write(f"TITLE: {Film_Name},IMDB: {imdb}")
    if st.button('Add To DataBase'):
                Final_Creat_db.insert_movie(Film_Name,imdb)
                st.success(f"✅ Fim {Film_Name} Added To Database successfully!")

elif option =='Add Movie From API':
    Film_id=st.number_input('Enter Movei Id ',min_value=1,max_value=250,step=1)
    result=app_api_list0.get_movei_info(Film_id)
    if Film_id!='':
        if st.button('Insert Movie'):
                st.write(f"TITLE: {result[0]},IMDB: {result[1]}")
        if st.button('Add To DataBase'):
                Final_Creat_db.insert_movie(result[0],result[1],result[2],result[3],\
                                            result[4],result[5],result[6],result[7])
                st.success(f"✅ Fim {result[0]} Added To Database successfully!")


elif option =='Movie Info By Name':
    Film_Name=st.text_input('Please Enter part or all of the movie name: ')
    if Film_Name!='':
        result=Final_Func_db.film_Search_Name(Film_Name)
        if st.button('Show Info'):
                st.write(f"The Number of Search Result is: {len(result)}.")
                Film_Result_Display(result, search_word=Film_Name)

elif option =='Movie Info By IMDB':
    min_imdb=st.number_input('Enter Minimum Of IMDB Rating : ',min_value=5,max_value=10,step=1)
    if min_imdb!='':
        result=Final_Func_db.imdb_range(min_imdb)
        if st.button('Show Info'):
                st.write(f"The Number of Search Result is: {len(result)}.")
                Film_Result_Display(result)

elif option=="Movie Info By Year Building" :
    min_year=st.number_input('Enter Minimum Of Year Build : ',min_value=1920,max_value=2026,step=1)
    if min_year!='':
        result=Final_Func_db.year_range(min_year)
        if st.button('Show Info'):
                st.write(f"The Number of Search Result is: {len(result)}.")
                Film_Result_Display(result)
elif option=='Sort Movie By Oscar Nominated' :
        result=Final_Func_db.Oscar_Nominated_Rating()
        if st.button('Show Info'):
                st.write(f"The Number of Search Result is: {len(result)}.")
                Film_Result_Display(result)
elif option=='Sort Movie By Oscar Won' :
        result=Final_Func_db.Oscar_Won_Rating()
        if st.button('Show Info'):
                st.write(f"The Number of Search Result is: {len(result)}.")
                Film_Result_Display(result)


elif option=="Movie Info By Country" :
    Country=st.selectbox('Select Country',('Iran',
        'USA','Mexico','Ireland', 'Canada'
        'England','Austria','Argentina',
        'UK','Denmark', 'Sweden',
        'France','Brazil','Poland',
        'Germany','Hong Kong',
        'Italy','South Korea',
        'Spain','Turkey',
        'Japan','Australia',
        'India','New Zealand'),index=0)
    country_name=Country
    result=Final_Func_db.list_country(country_name)
    if st.button('Show Info'):
            st.write(f"The Number of Search Result is: {len(result)}.")
            Film_Result_Display(result)
   


elif option =='Delete film':
    film_id=st.number_input('Enter id to delete film : ',min_value=1,max_value=250,step=1)
    if film_id !='':
        Final_Func_db.delete_records(film_id)
        result=Final_Func_db.select_all_records()
        if st.button('Delete Film'):
               st.write(f"The film number  {film_id} is deleted.")
               st.write(f"The Number of Search Result is: {len(result)}.")
               Film_Result_Display(result)
               
          

elif option =='Edit Film':
    film_id=st.number_input('Enter id to Edit film : ',min_value=1,max_value=250,step=1)
    imdb_input = st.number_input('Enter Your IMDB: ', min_value=5.0, max_value=10.0, step=0.1)
    result=Final_Func_db.select_all_records()
    if film_id in [result[i][0] for i in range(len(result))]:
        Final_Func_db.update_record_by_id(film_id,imdb_input)
        result=Final_Func_db.select_all_records()
        if st.button('Edit Film'):
               st.write(f"The film number  {film_id} is Edited to New IMDB {imdb_input}.")
               st.write(f"The Number of Search Result is: {len(result)}.")
               Film_Result_Display(result)
    else:
          if st.button('Show Info'):
               st.error(f"Film id {film_id} not found!")

                                  
elif option =='Restore Default':
        Final_Func_db.Restore_Default()
        result=Final_Func_db.select_all_records()
        if st.button('Restore Films To Default'):
                st.success("✅ Database restored to default successfully!")
                st.balloons()
                st.write(f"The Number of Search Result is: {len(result)}.")
                Film_Result_Display(result)
