from django.urls import path
import analytics.views as analytics_views

urlpatterns = [
    path('analytics/', analytics_views.get_aggregated_data, name='analytics'),
    path('dashboard/plotly/', analytics_views.plotly_dashboard, name='plotly_dashboard'),
    path('dashboard/bokeh/', analytics_views.bokeh_dashboard, name='bokeh_dashboard'),
    path('analytics/average_order_value/', analytics_views.get_average_order_value, name='average_order_value'),
    path('analytics/orders_by_month/', analytics_views.get_orders_by_month, name='orders_by_month'),
    path('analytics/average_discount/', analytics_views.get_average_discount_by_category, name='average_discount'),
    path('analytics/top_products/', analytics_views.get_top_selling_products, name='top_products'),
    path('analytics/revenue_by_customer/', analytics_views.get_revenue_by_customer, name='revenue_by_customer'),
    path('dashboard/', analytics_views.dashboard_view, name='dashboard_view'),

    path('dashboard/plotly/sales_by_category/', analytics_views.plotly_sales_by_category, name='plotly_sales_by_category'),
    path('dashboard/plotly/sales_pie/', analytics_views.plotly_sales_pie, name='plotly_sales_pie'),
    path('dashboard/plotly/orders_by_month/', analytics_views.plotly_orders_by_month, name='plotly_orders_by_month'),
    path('dashboard/plotly/average_order_value/', analytics_views.plotly_average_order_value, name='plotly_average_order_value'),
    path('dashboard/plotly/top_selling_products/', analytics_views.plotly_top_selling_products, name='plotly_top_selling_products'),
    path('dashboard/plotly/average_discount/', analytics_views.plotly_average_discount, name='plotly_average_discount'),
    path('dashboard/bokeh/sales_by_category/', analytics_views.bokeh_sales_by_category, name='bokeh_sales_by_category'),
    path('dashboard/bokeh/sales_pie/', analytics_views.bokeh_sales_pie, name='bokeh_sales_pie'),
    path('dashboard/bokeh/orders_by_month/', analytics_views.bokeh_orders_by_month, name='bokeh_orders_by_month'),
    path('dashboard/bokeh/average_order_value/', analytics_views.bokeh_average_order_value, name='bokeh_average_order_value'),
    path('dashboard/bokeh/top_selling_products/', analytics_views.bokeh_top_selling_products, name='bokeh_top_selling_products'),
    path('dashboard/bokeh/average_discount/', analytics_views.bokeh_average_discount, name='bokeh_average_discount'),
]
