

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read data
def read(name):
    '''
    reading data from read function
    '''
    # read data
    df = pd.read_csv(name,skiprows=4)
    
    origdata=df.drop(['Country Code', 'Indicator Code'],axis=1)
    
    countdata=df.drop(['Country Code', 'Indicator Name', 'Indicator Code'],axis=1)
    
    yedata= df.drop(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code',],axis=1).T
    
    yedata.index.name='Years'
    
    # print the data of head
    print(yedata.head)
    print(countdata.head)
    print(origdata.head)
    print(origdata.T)
    
    # return data value of year and column
    return countdata,yedata,origdata

    # plot a lie graph
def agriculture_line_graph(data,indicator,indicator_name):
    '''
    this function plot graph line plot of specific country 
    '''
    # create a dataframe
    fdata=data[data["Indicator Name"]==indicator]
    
    uk=fdata[fdata["Country Name"]=="United Kingdom"].drop(['Country Name','Indicator Name'],axis=1)

    latvia=fdata[fdata["Country Name"]=="Latvia"].drop(['Country Name','Indicator Name'],axis=1)
    
    morocco=fdata[fdata["Country Name"]=="Morocco"].drop(['Country Name','Indicator Name'],axis=1)
    
    mexico=fdata[fdata["Country Name"]=="Mexico"].drop(['Country Name','Indicator Name'],axis=1)
  
    # year data frame
    year=data.drop(['Country Name','Indicator Name'],axis=1).T.index
    
    print(year)
    
    # plotting the points 
    plt.plot(pd.to_numeric(year[0:62].to_numpy()),uk.iloc[0].dropna().to_numpy() , label = "United Kingdom",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:62].to_numpy()),latvia.iloc[0].dropna().to_numpy() , label = "latvia",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:62].to_numpy()),morocco.iloc[0].dropna().to_numpy() , label = "Morocco",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:62].to_numpy()),mexico.iloc[0].dropna().to_numpy() , label = "Mexico",linestyle="-.")
    
      
    # x axis name
    plt.xlabel('year')
    # naming the y axis
    plt.ylabel('data')
    plt.legend()
    # title of graph
    plt.title(indicator_name)
      
    # function to show the plot
    plt.show()
    
def urban_line_graph(data,indicator,indicator_name):
    '''
    this function plot graph line plot of 4 country
    '''
    # create a dataframe
    fdata=data[data["Indicator Name"]==indicator]
    
    uk=fdata[fdata["Country Name"]=="United Kingdom"].drop(['Country Name','Indicator Name'],axis=1)

    latvia=fdata[fdata["Country Name"]=="Latvia"].drop(['Country Name','Indicator Name'],axis=1)
    
    morocco=fdata[fdata["Country Name"]=="Morocco"].drop(['Country Name','Indicator Name'],axis=1)
    
    mexico=fdata[fdata["Country Name"]=="Mexico"].drop(['Country Name','Indicator Name'],axis=1)
  
    # year data frame
    year=data.drop(['Country Name','Indicator Name'],axis=1).T.index
    
    print(year)
    
    # plotting the points 
    plt.plot(pd.to_numeric(year[0:62].to_numpy()),uk.iloc[0].dropna().to_numpy() , label = "United Kingdom",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:62].to_numpy()),latvia.iloc[0].dropna().to_numpy() , label = "latvia",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:62].to_numpy()),morocco.iloc[0].dropna().to_numpy() , label = "Morocco",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:62].to_numpy()),mexico.iloc[0].dropna().to_numpy() , label = "Mexico",linestyle="-.")
    
      
    # x axis name
    plt.xlabel('year')
    # naming the y axis
    plt.ylabel('data')
    plt.legend()
    # title of graph
    plt.title(indicator_name)
      
    # function to show the plot
    plt.show()
    
   
    
 # plot a bar graoh  
def agriculture_bar_plot(data,indicator,indicator_name):
    '''
    function will show bar plot graph for the 4 countries year 1996 to 2016
    '''
    #  creating a data frame
    fdata=data[data["Indicator Name"]==indicator]
    
    uk=fdata[fdata["Country Name"]=="United Kingdom"].drop(['Country Name','Indicator Name'],axis=1)

    latvia=fdata[fdata["Country Name"]=="Latvia"]
    
    morocco=fdata[fdata["Country Name"]=="Morocco"]
    
    mexico=fdata[fdata["Country Name"]=="Mexico"]
    
    index = ['1996', '2000', '2004',
          '2008', '2012', '2016']
    
    df = pd.DataFrame({'latvia':  [latvia['1996'].iloc[0],latvia['2000'].iloc[0],latvia['2004'].iloc[0],latvia['2008'].iloc[0],latvia['2012'].iloc[0],latvia['2016'].iloc[0],],
                       'Morocco': [morocco['1996'].iloc[0],morocco['2000'].iloc[0],morocco['2004'].iloc[0],morocco['2008'].iloc[0],morocco['2012'].iloc[0],morocco['2016'].iloc[0],],
                       'United Kingdom':  [uk['1996'].iloc[0],uk['2000'].iloc[0],uk['2004'].iloc[0],uk['2008'].iloc[0],uk['2012'].iloc[0],uk['2016'].iloc[0],],
                    'Mexico':  [mexico['1996'].iloc[0],mexico['2000'].iloc[0],mexico['2004'].iloc[0],mexico['2008'].iloc[0],mexico['2012'].iloc[0],mexico['2016'].iloc[0],],
                    
                    }, index=index)
    
    # ploting bar graph
    ax = df.plot.barh(title=indicator_name)
    
    plt.show()
    
def mortality_bar_plot(data,indicator,indicator_name):
    '''
    this function show bar plot graph for the 4 countries year 1996 to 2016
    '''
    #  creating a data frame
    fdata=data[data["Indicator Name"]==indicator]
    
    uk=fdata[fdata["Country Name"]=="United Kingdom"].drop(['Country Name','Indicator Name'],axis=1)

    latvia=fdata[fdata["Country Name"]=="Latvia"]
    
    morocco=fdata[fdata["Country Name"]=="Morocco"]
    
    mexico=fdata[fdata["Country Name"]=="Mexico"]
    
    index = ['1996', '2000', '2004',
          '2008', '2012', '2016']
    
    df = pd.DataFrame({'latvia':  [latvia['1996'].iloc[0],latvia['2000'].iloc[0],latvia['2004'].iloc[0],latvia['2008'].iloc[0],latvia['2012'].iloc[0],latvia['2016'].iloc[0],],
                       'Morocco': [morocco['1996'].iloc[0],morocco['2000'].iloc[0],morocco['2004'].iloc[0],morocco['2008'].iloc[0],morocco['2012'].iloc[0],morocco['2016'].iloc[0],],
                    'United Kingdom':  [uk['1996'].iloc[0],uk['2000'].iloc[0],uk['2004'].iloc[0],uk['2008'].iloc[0],uk['2012'].iloc[0],uk['2016'].iloc[0],],
                    'Mexico':  [mexico['1996'].iloc[0],mexico['2000'].iloc[0],mexico['2004'].iloc[0],mexico['2008'].iloc[0],mexico['2012'].iloc[0],mexico['2016'].iloc[0],],
                    
                    }, index=index)
    
    # ploting bar graph
    ax = df.plot.barh(title=indicator_name)
    
    plt.show()

# plot a heatmap with annotation
def latvia_correlation_heatmap(data,name):
    '''
    this function show heatmap and correlations of latvia between indicators for better understanding
    '''
    
    #conditions applied on country name
        
    # create data frame
    fdata=pd.DataFrame()
        
    # getting indicator data
    latviadata=data[data["Indicator Name"]=="Urban population"]
        
    # get united states data 
    latviaurban=latviadata[latviadata['Country Name']=="Latvia"].drop(['Country Name','Indicator Name'],axis=1).T
        
    # drop nan values
    latviaurban=latviaurban.dropna().T
        
    # get urban population data
    fdata["Urban population"]=latviaurban.iloc[0]
        
    #  get arable data
    latviadata=data[data["Indicator Name"]=='Agricultural land (sq. km)']
        
        
    latviaurban=latviadata[latviadata['Country Name']=="Latvia"].drop(['Country Name','Indicator Name'],axis=1).T
        
    latviaurban=latviaurban.dropna().T
        
    fdata['Agricultural land (sq. km)']=latviaurban.iloc[0]
        
    #  get cereal data
    latviadata=data[data["Indicator Name"]=='Mortality rate, under-5 (per 1,000 live births)']
        
    latviaurban=latviadata[latviadata['Country Name']=="Latvia"].drop(['Country Name','Indicator Name'],axis=1).T
        
    latviaurban=latviaurban.dropna().T
        
    fdata['Mortality rate, under-5 (per 1,000 live births)']=latviaurban.iloc[0]
        
    latviadata=data[data["Indicator Name"]=='Population, total']
    
    latviaurban=latviadata[latviadata['Country Name']=="Latvia"].drop(['Country Name','Indicator Name'],axis=1).T
        
    latviaurban=latviaurban.dropna().T
    
    fdata['Population, total']=latviaurban.iloc[0]
        
    # plot a heatmap with annotation
        
    ax = plt.axes()
        
    # ploting heatmap
    heatmap = sns.heatmap(fdata.corr(), cmap="tab10",
                             
        annot=True,ax=ax
                
                )
        # add title
    ax.set_title('Latvia')
        
    plt.show()
    
def uk_correlation_heatmap(data,name):
    '''
    this function show heatmap and correlations of uk between indicators for better understanding
    '''
    
   
    # get dataframe
    fdata=pd.DataFrame()
        
    # get urban population
    ukdata=data[data["Indicator Name"]=="Urban population"]
        
    # get UK data
    ukurban=ukdata[ukdata['Country Name']=="United Kingdom"].drop(['Country Name','Indicator Name'],axis=1).T
        
    # drop nan value
    ukurban=ukurban.dropna().T
        
    fdata["Urban population"]=ukurban.iloc[0]
        
    ukdata=data[data["Indicator Name"]=='Agricultural land (sq. km)']
        
    ukurban=ukdata[ukdata['Country Name']=="United Kingdom"].drop(['Country Name','Indicator Name'],axis=1).T
        
    ukurban=ukurban.dropna().T
        
    # get arabledata
    fdata['Agricultural land (sq. km)']=ukurban.iloc[0]
        
    # get cereal data
    ukdata=data[data["Indicator Name"]=='Mortality rate, under-5 (per 1,000 live births)']
        
    ukurban=ukdata[ukdata['Country Name']=="United Kingdom"].drop(['Country Name','Indicator Name'],axis=1).T
    
    ukurban=ukurban.dropna().T
        
    fdata['Mortality rate, under-5 (per 1,000 live births)']=ukurban.iloc[0]
        
    ukdata=data[data["Indicator Name"]=='Population, total']
        
    ukurban=ukdata[ukdata['Country Name']=="United Kingdom"].drop(['Country Name','Indicator Name'],axis=1).T
        
    ukurban=ukurban.dropna().T
        
    # get total population
    fdata['Population, total']=ukurban.iloc[0]
        
    # plot a heatmap with annotation
    ax = plt.axes()
        
        # plot heat map
    heatmap = sns.heatmap(fdata.corr(), cmap="tab10",
        annot=True,ax=ax
                
        )
        
        # set title
    ax.set_title('United Kingdom')
        
    plt.show()
        
def morocco_correlation_heatmap(data,name):
    '''
    this function show heatmap of and correlations of morocco between indicators for better understanding
    '''
        
    # crete panda dataframe
    fdata=pd.DataFrame()
        
    #  get uk urba  population  data
    moroccodata=data[data["Indicator Name"]=="Urban population"]
        
    moroccourban=moroccodata[moroccodata['Country Name']=="Morocco"].drop(['Country Name','Indicator Name'],axis=1).T
        
    # drop nan value
    moroccourban=moroccourban.dropna().T
        
    fdata["Urban population"]=moroccourban.iloc[0]
        
    # get arable data
    moroccodata=data[data["Indicator Name"]=='Agricultural land (sq. km)']
        
    moroccourban=moroccodata[moroccodata['Country Name']=="Morocco"].drop(['Country Name','Indicator Name'],axis=1).T
        
    moroccourban=moroccourban.dropna().T
        
    fdata['Agricultural land (sq. km)']=moroccourban.iloc[0]
        
    moroccodata=data[data["Indicator Name"]=='Mortality rate, under-5 (per 1,000 live births)']
        
    moroccourban=moroccodata[moroccodata['Country Name']=="Morocco"].drop(['Country Name','Indicator Name'],axis=1).T
        
    moroccourban=moroccourban.dropna().T
        
    #  cereal yield data
    fdata['Mortality rate, under-5 (per 1,000 live births)']=moroccourban.iloc[0]
        
    #  get total population data
    moroccodata=data[data["Indicator Name"]=='Population, total']
        
    moroccourban=moroccodata[moroccodata['Country Name']=="Morocco"].drop(['Country Name','Indicator Name'],axis=1).T
        
    moroccourban=moroccourban.dropna().T
        
    fdata['Population, total']=moroccourban.iloc[0]
        
    # plot a heatmap with annotation
    ax = plt.axes()
        
    heatmap = sns.heatmap(fdata.corr(), cmap="tab10",
        annot=True,ax=ax
                
        )
        
    # set title
    ax.set_title('Morocco')
    plt.show()  
        
def mexico_correlation_heatmap(data,name):
    '''
    this function show heatmap of and correlations of mexico between indicators for better understanding
    '''
        
    # get dataframe
    fdata=pd.DataFrame()
        
    # uk urban population
    mexicodata=data[data["Indicator Name"]=="Urban population"]
        
    # uk data
    mexicourban=mexicodata[mexicodata['Country Name']=="Mexico"].drop(['Country Name','Indicator Name'],axis=1).T
        
    mexicourban=mexicourban.dropna().T
    
    #  urban data
    fdata["Urban population"]=mexicourban.iloc[0]
        
    mexicodata=data[data["Indicator Name"]=='Agricultural land (sq. km)']
        
    mexicourban=mexicodata[mexicodata['Country Name']=="Mexico"].drop(['Country Name','Indicator Name'],axis=1).T
        
    # drop nan value
    mexicourban=mexicourban.dropna().T
        
    fdata['Agricultural land (sq. km)']=mexicourban.iloc[0]
        
    mexicodata=data[data["Indicator Name"]=='Mortality rate, under-5 (per 1,000 live births)']
        
    mexicourban=mexicodata[mexicodata['Country Name']=="Mexico"].drop(['Country Name','Indicator Name'],axis=1).T
        
    mexicourban=mexicourban.dropna().T
        
    fdata['Mortality rate, under-5 (per 1,000 live births)']=mexicourban.iloc[0]
        
    mexicodata=data[data["Indicator Name"]=='Population, total']
        
    mexicourban=mexicodata[mexicodata['Country Name']=="Mexico"].drop(['Country Name','Indicator Name'],axis=1).T
        
    mexicourban=mexicourban.dropna().T
        
    #  population data
    fdata['Population, total']=mexicourban.iloc[0]
        
    # plot a heatmap with annotation
    ax = plt.axes()
        
    heatmap = sns.heatmap(fdata.corr(), cmap="tab10",
        annot=True,ax=ax
        )
        
    #  set title
    ax.set_title('Mexico')
        
    plt.show()  
                       
    
    # that is main function
if __name__ == "__main__":
    
    coundata,yedata,origdata=read("api.csv")
    
    agriculture_bar_plot(origdata,'Agricultural land (sq. km)','Agricultural land (sq. km)')
    
    mortality_bar_plot(origdata,'Mortality rate, under-5 (per 1,000 live births)','Mortality rate, under-5 (per 1,000 live births)')
    
    agriculture_line_graph(origdata, 'Population, total','Population, total')
    
    urban_line_graph(origdata, 'Urban population','Urban population')
    
    latvia_correlation_heatmap(origdata,"latvia")
    
    uk_correlation_heatmap(origdata,"uk")
    
    morocco_correlation_heatmap(origdata,"morocco")
    
    mexico_correlation_heatmap(origdata,"mexico")
