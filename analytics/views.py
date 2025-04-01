from django.db.models.functions import TruncMonth
from django.urls import path
import analytics.views as analytics_views
from django.db.models import Avg, Sum, Min, Max, F, Count
from rest_framework.response import Response
from rest_framework.decorators import api_view
import pandas as pd
import plotly.express as px
import bokeh.plotting as bp
from order.models import OrderItem, Order
from django.shortcuts import render
from bokeh.embed import components
from bokeh.transform import cumsum
from bokeh.palettes import Category20c


@api_view(['GET'])
def get_aggregated_data(request):
    data = OrderItem.objects.values('product__category__name').annotate(
        total_sales=Sum('quantity'),
        avg_price=Avg('product__price'),
        min_price=Min('product__price'),
        max_price=Max('product__price'),
        total_revenue=Sum(F('quantity') * F('product__price'))
    )
    df = pd.DataFrame(list(data))
    return Response(df.to_json(orient='records'))


@api_view(['GET'])
def plotly_dashboard(request):
    data = OrderItem.objects.values('product__category__name').annotate(total_sales=Sum('quantity'))
    df = pd.DataFrame(list(data))
    fig = px.bar(df, x='product__category__name', y='total_sales', title='Total Sales by Category')
    return Response(fig.to_json())


@api_view(['GET'])
def get_average_order_value(request):
    data = Order.objects.values('user__id').annotate(avg_order_value=Avg('total_price'))
    df = pd.DataFrame(list(data))
    df['avg_order_value'] = df['avg_order_value'].astype(float)
    return Response(df.to_json(orient='records'))


@api_view(['GET'])
def get_orders_by_month(request):
    data = Order.objects.annotate(month=TruncMonth('created_at')).values('month').annotate(
        total_orders=Count('id')).order_by('month')
    df = pd.DataFrame(list(data))
    df['month'] = df['month'].dt.strftime('%Y-%m')
    return Response(df.to_json(orient='records'))


@api_view(['GET'])
def get_average_discount_by_category(request):
    data = OrderItem.objects.values('product__category__name').annotate(avg_discount=Avg(F('discount')))
    df = pd.DataFrame(list(data))
    df['avg_discount'] = df['avg_discount'].astype(float)
    return Response(df.to_json(orient='records'))


@api_view(['GET'])
def get_top_selling_products(request):
    data = OrderItem.objects.values('product__name').annotate(total_sales=Sum('quantity')).order_by('-total_sales')[:5]
    df = pd.DataFrame(list(data))
    return Response(df.to_json(orient='records'))


@api_view(['GET'])
def get_revenue_by_customer(request):
    data = Order.objects.values('user__id').annotate(total_revenue=Sum('total_price'))
    df = pd.DataFrame(list(data))
    return Response(df.to_json(orient='records'))


@api_view(['GET'])
def bokeh_dashboard(request):
    data = OrderItem.objects.values('product__category__name').annotate(total_sales=Sum('quantity'))
    df = pd.DataFrame(list(data))
    p = bp.figure(title='Total Sales by Category', x_range=df['product__category__name'].tolist(), height=350,
                  toolbar_location=None, tools="")
    p.vbar(x=df['product__category__name'], top=df['total_sales'], width=0.9)

    script, div = components(p)
    return Response({'script': script, 'div': div})


def dashboard_view(request):
    return render(request, 'dashboard.html')


@api_view(['GET'])
def plotly_sales_by_category(request):
    data = OrderItem.objects.values('product__category__name').annotate(total_sales=Sum('quantity'))
    df = pd.DataFrame(list(data))
    fig = px.bar(df, x='product__category__name', y='total_sales', title='Total Sales by Category')
    return Response(fig.to_json())


@api_view(['GET'])
def bokeh_sales_by_category(request):
    data = OrderItem.objects.values('product__category__name').annotate(total_sales=Sum('quantity'))
    df = pd.DataFrame(list(data))
    p = bp.figure(title='Total Sales by Category', x_range=df['product__category__name'].tolist(), height=350, toolbar_location=None, tools="")
    p.vbar(x=df['product__category__name'], top=df['total_sales'], width=0.9)
    script, div = components(p)
    return Response({'script': script, 'div': div})


@api_view(['GET'])
def plotly_sales_pie(request):
    data = OrderItem.objects.values('product__category__name').annotate(total_sales=Sum('quantity'))
    df = pd.DataFrame(list(data))
    fig = px.pie(df, names='product__category__name', values='total_sales', title='Sales Distribution by Category')
    return Response(fig.to_json())


@api_view(['GET'])
def bokeh_sales_pie(request):
    data = OrderItem.objects.values('product__category__name').annotate(total_sales=Sum('quantity'))
    df = pd.DataFrame(list(data))
    p = bp.figure(title="Sales Distribution by Category", toolbar_location=None, tools="")

    p.wedge(x=0, y=1, radius=0.4, start_angle=cumsum('total_sales', include_zero=True), end_angle=cumsum('total_sales'),
            line_color="white", fill_color=Category20c[len(df)])
    p.axis.visible = False
    p.grid.visible = False
    script, div = components(p)
    return Response({'script': script, 'div': div})


@api_view(['GET'])
def plotly_orders_by_month(request):
    data = Order.objects.annotate(month=TruncMonth('created_at')).values('month').annotate(total_orders=Count('id')).order_by('month')
    df = pd.DataFrame(list(data))
    df['month'] = df['month'].dt.strftime('%Y-%m')
    fig = px.line(df, x='month', y='total_orders', title='Orders by Month')
    return Response(fig.to_json())


@api_view(['GET'])
def bokeh_orders_by_month(request):
    data = Order.objects.annotate(month=TruncMonth('created_at')).values('month').annotate(total_orders=Count('id')).order_by('month')
    df = pd.DataFrame(list(data))
    df['month'] = df['month'].dt.strftime('%Y-%m')
    p = bp.figure(title="Orders by Month", x_axis_type="datetime", height=350, toolbar_location=None, tools="")
    p.line(df['month'], df['total_orders'], line_width=2)
    p.xaxis.axis_label = 'Month'
    p.yaxis.axis_label = 'Total Orders'
    script, div = components(p)
    return Response({'script': script, 'div': div})


@api_view(['GET'])
def plotly_average_order_value(request):
    data = Order.objects.values('user__id').annotate(avg_order_value=Avg('total_price'))
    df = pd.DataFrame(list(data))
    fig = px.bar(df, x='user__id', y='avg_order_value', title='Average Order Value by User')
    return Response(fig.to_json())


@api_view(['GET'])
def bokeh_average_order_value(request):
    data = Order.objects.values('user__id').annotate(avg_order_value=Avg('total_price'))
    df = pd.DataFrame(list(data))
    df['avg_order_value'] = df['avg_order_value'].astype(float)
    p = bp.figure(title='Average Order Value by User', x_range=df['user__id'].astype(str).tolist(), height=350, toolbar_location=None, tools="")
    p.vbar(x=df['user__id'], top=df['avg_order_value'], width=0.9)
    p.xaxis.axis_label = 'User ID'
    p.yaxis.axis_label = 'Average Order Value'
    script, div = components(p)
    return Response({'script': script, 'div': div})


@api_view(['GET'])
def plotly_top_selling_products(request):
    data = OrderItem.objects.values('product__name').annotate(total_sales=Sum('quantity')).order_by('-total_sales')[:5]
    df = pd.DataFrame(list(data))
    fig = px.bar(df, x='product__name', y='total_sales', title='Top Selling Products')
    return Response(fig.to_json())


@api_view(['GET'])
def bokeh_top_selling_products(request):
    data = OrderItem.objects.values('product__name').annotate(total_sales=Sum('quantity')).order_by('-total_sales')[:5]
    df = pd.DataFrame(list(data))
    p = bp.figure(title='Top Selling Products', x_range=df['product__name'].tolist(), height=350, toolbar_location=None, tools="")
    p.vbar(x=df['product__name'], top=df['total_sales'], width=0.9)
    p.xaxis.axis_label = 'Product Name'
    p.yaxis.axis_label = 'Total Sales'
    script, div = components(p)
    return Response({'script': script, 'div': div})


@api_view(['GET'])
def plotly_average_discount(request):
    data = OrderItem.objects.values('product__category__name').annotate(avg_discount=Avg(F('discount')))
    df = pd.DataFrame(list(data))
    fig = px.pie(df, names='product__category__name', values='avg_discount', title='Average Discount by Category')
    return Response(fig.to_json())


@api_view(['GET'])
def bokeh_average_discount(request):
    data = OrderItem.objects.values('product__category__name').annotate(avg_discount=Avg(F('discount')))
    df = pd.DataFrame(list(data))

    df['avg_discount'] = df['avg_discount'].astype(float)

    p = bp.figure(title='Average Discount by Category', x_range=df['product__category__name'].tolist(), height=350, toolbar_location=None, tools="")
    p.vbar(x=df['product__category__name'], top=df['avg_discount'], width=0.9)
    p.xaxis.axis_label = 'Category'
    p.yaxis.axis_label = 'Average Discount'
    script, div = components(p)
    return Response({'script': script, 'div': div})
