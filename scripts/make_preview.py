"""Create a recruiter-friendly *synthetic only* PNG dashboard from local demo output."""
import json
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

base=Path('output/demo')
result=json.loads((base/'quality_and_kpis.json').read_text())
monthly=pd.read_csv(base/'monthly_sales.csv')
countries=pd.read_csv(base/'country_sales.csv')
kpi=result['kpis']

fig=plt.figure(figsize=(15,8.2),facecolor='#0e1726')
gs=GridSpec(3,2,figure=fig,height_ratios=[1.18,2.2,.6],hspace=.45,wspace=.25,left=.07,right=.95,top=.86,bottom=.08)
fig.text(.067,.955,'RETAIL INTELLIGENCE  /  CASE STUDY',color='#d8e5ef',fontsize=12,fontweight='bold')
fig.text(.067,.90,'Sales, returns & data quality',color='white',fontsize=25,fontweight='bold')
fig.text(.95,.91,'SYNTHETIC DEMO DATA  •  NOT ACTUAL UCI RESULTS',color='#ffce7a',fontsize=10,fontweight='bold',ha='right')
metrics=[('GROSS SALES',f"£{kpi['gross_sales_gbp']:,.0f}"),('ORDERS',f"{kpi['orders']:,}"),('AVG ORDER',f"£{kpi['average_order_value_gbp']:,.2f}"),('CANCELLED VALUE',f"£{kpi['cancellation_line_value_gbp']:,.0f}")]
card_y=.68
for i,(label,value) in enumerate(metrics):
 x=.07+i*.228
 from matplotlib.patches import FancyBboxPatch
 box=FancyBboxPatch((x,card_y),.204,.108,boxstyle='round,pad=0.007,rounding_size=0.012',facecolor='#1d2e42',edgecolor='#314a62',transform=fig.transFigure)
 fig.patches.append(box)
 fig.text(x+.015,card_y+.075,label,color='#a9bbcc',fontsize=10,weight='bold',transform=fig.transFigure)
 fig.text(x+.015,card_y+.023,value,color='white',fontsize=20,weight='bold',transform=fig.transFigure)
ax1=fig.add_subplot(gs[1,0],facecolor='#17283d')
ax2=fig.add_subplot(gs[1,1],facecolor='#17283d')
for ax in (ax1,ax2):
 for side in ('top','right','left'):ax.spines[side].set_visible(False)
 ax.spines['bottom'].set_color('#68849c')
 ax.tick_params(colors='#d8e5ef')
 ax.grid(axis='y',color='#47617b',alpha=.35)
 ax.set_axisbelow(True)
ax1.plot(monthly['month'].astype(str),monthly['line_revenue_gbp']/1000,color='#4fd8c3',marker='o',lw=2.5)
ax1.set_title('Gross sales by month',loc='left',pad=16,color='white',weight='bold',fontsize=14)
ax1.set_ylabel('GBP, thousands',color='#c0d0de')
ax1.tick_params(axis='x',rotation=45)
ax2.barh(countries.head(5)['Country'].iloc[::-1].astype(str),countries.head(5)['revenue_gbp'].iloc[::-1]/1000,color='#55b8f3')
ax2.set_title('Top 5 countries by gross sales',loc='left',pad=16,color='white',weight='bold',fontsize=14)
ax2.set_xlabel('GBP, thousands',color='#c0d0de')
fig.text(.07,.09,'Business rules: positive-quantity sales only • cancellations reported separately • duplicate rows excluded • validated with SQL',color='#c1d2df',fontsize=10)
out=Path('preview/retail_demo_dashboard.png')
out.parent.mkdir(exist_ok=True)
fig.savefig(out,dpi=140,facecolor=fig.get_facecolor())
plt.close(fig)
print(out)
