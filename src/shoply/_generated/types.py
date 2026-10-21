# Written by scripts/generate.py from the API reference. Do not edit by hand.
#
# What a route answers is read off an answer the route gave, as the reference's is: a field that
# was text there may be None in another answer, and a route with no recorded answer answers Any.

from typing import Any, Dict, List, Literal, Optional, TypedDict, Union

KeyShowResultKey = TypedDict("KeyShowResultKey", {
    "id": str,
    "name": str,
    "prefix": str,
    "scopes": List[str],
    "allowedIps": Union[List[Any], Dict[str, Any]],
    "allowedDomains": Union[List[Any], Dict[str, Any]],
    "expiresAt": Any,
    "expired": bool,
    "createdAt": str,
    "lastUsedAt": Any,
    "revokedAt": Any,
})

KeyShowResultStore = TypedDict("KeyShowResultStore", {
    "id": str,
    "name": str,
    "slug": str,
    "url": str,
})

KeyShowResult = TypedDict("KeyShowResult", {
    "key": KeyShowResultKey,
    "store": KeyShowResultStore,
    "api": str,
})

StoreShowResultSocialLinks = TypedDict("StoreShowResultSocialLinks", {
    "discord": str,
    "youtube": str,
    "tiktok": str,
    "x": str,
    "instagram": str,
    "telegram": str,
})

StoreShowResultCurrenciesItem = TypedDict("StoreShowResultCurrenciesItem", {
    "code": str,
    "name": str,
})

StoreShowResult = TypedDict("StoreShowResult", {
    "id": str,
    "name": str,
    "slug": str,
    "urlChangeableAt": Any,
    "supportUrl": str,
    "guideUrl": str,
    "panelUrl": str,
    "socialLinks": StoreShowResultSocialLinks,
    "customLinks": Union[List[Any], Dict[str, Any]],
    "description": str,
    "currencyCode": str,
    "adaptivePricing": bool,
    "currencies": List[StoreShowResultCurrenciesItem],
    "ratesFetchedAt": str,
    "locale": str,
    "logoUrl": Any,
    "faviconUrl": Any,
    "storefrontPassword": str,
    "storefrontPasswordUnreadable": bool,
    "accentColor": str,
    "theme": str,
    "publishStock": bool,
    "lowStockThreshold": float,
    "dashboardCards": List[str],
    "termsOfService": str,
    "refundPolicy": str,
    "autoReviews": bool,
    "publicStats": bool,
    "saleNotifications": bool,
    "publicOnline": bool,
    "active": bool,
    "blocked": Any,
    "businessType": str,
    "businessName": str,
    "businessTaxId": str,
    "businessVatNumber": str,
    "businessLine1": str,
    "businessLine2": str,
    "businessCity": str,
    "businessRegion": str,
    "businessPostalCode": str,
    "businessCountry": str,
    "invoiceFooter": str,
    "originCountry": str,
    "hasDynamicSecret": bool,
    "dynamicSecretEnd": str,
    "updatedAt": str,
})

StoreUpdateResultSocialLinks = TypedDict("StoreUpdateResultSocialLinks", {
    "discord": str,
    "youtube": str,
    "tiktok": str,
    "x": str,
    "instagram": str,
    "telegram": str,
})

StoreUpdateResultCurrenciesItem = TypedDict("StoreUpdateResultCurrenciesItem", {
    "code": str,
    "name": str,
})

StoreUpdateResult = TypedDict("StoreUpdateResult", {
    "id": str,
    "name": str,
    "slug": str,
    "urlChangeableAt": Any,
    "supportUrl": str,
    "guideUrl": str,
    "panelUrl": str,
    "socialLinks": StoreUpdateResultSocialLinks,
    "customLinks": Union[List[Any], Dict[str, Any]],
    "description": str,
    "currencyCode": str,
    "adaptivePricing": bool,
    "currencies": List[StoreUpdateResultCurrenciesItem],
    "ratesFetchedAt": str,
    "locale": str,
    "logoUrl": Any,
    "faviconUrl": Any,
    "storefrontPassword": str,
    "storefrontPasswordUnreadable": bool,
    "accentColor": str,
    "theme": str,
    "publishStock": bool,
    "lowStockThreshold": float,
    "dashboardCards": List[str],
    "termsOfService": str,
    "refundPolicy": str,
    "autoReviews": bool,
    "publicStats": bool,
    "saleNotifications": bool,
    "publicOnline": bool,
    "active": bool,
    "blocked": Any,
    "businessType": str,
    "businessName": str,
    "businessTaxId": str,
    "businessVatNumber": str,
    "businessLine1": str,
    "businessLine2": str,
    "businessCity": str,
    "businessRegion": str,
    "businessPostalCode": str,
    "businessCountry": str,
    "invoiceFooter": str,
    "originCountry": str,
    "hasDynamicSecret": bool,
    "dynamicSecretEnd": str,
    "updatedAt": str,
})

StoreEmailSettingsResultTestEmailEvery = TypedDict("StoreEmailSettingsResultTestEmailEvery", {
    "limit": float,
    "window": float,
})

StoreEmailSettingsResult = TypedDict("StoreEmailSettingsResult", {
    "fromName": str,
    "replyTo": str,
    "defaultInstructions": str,
    "buttons": Union[List[Any], Dict[str, Any]],
    "buttonDefaultLabel": str,
    "maxButtons": float,
    "panelButtonUrl": str,
    "autoReviews": bool,
    "firstOrderCouponEnabled": bool,
    "firstOrderCouponPercent": float,
    "firstOrderCouponDays": float,
    "firstOrderCouponDelivery": str,
    "firstOrderCouponDelayMinutes": float,
    "firstOrderCouponPrefix": str,
    "maxFirstOrderPercent": float,
    "maxFirstOrderDays": float,
    "notifyEnabled": bool,
    "notifyAddress": str,
    "emailStockEnabled": bool,
    "emailStockThreshold": float,
    "emailPayoutsEnabled": bool,
    "emailCustomPaidEnabled": bool,
    "emailDisputeOpenedEnabled": bool,
    "emailDisputeClosedEnabled": bool,
    "testEmailEvery": StoreEmailSettingsResultTestEmailEvery,
    "discordWebhookSet": bool,
    "discordWebhookMasked": str,
    "discordOrdersEnabled": bool,
    "discordStockEnabled": bool,
    "discordErrorsEnabled": bool,
    "discordReviewsEnabled": bool,
    "discordPayoutsEnabled": bool,
    "discordCustomPaidEnabled": bool,
    "discordDisputesEnabled": bool,
    "discordStockThreshold": float,
    "discordFailure": Any,
    "storeName": str,
    "emailAccent": str,
    "updatedAt": str,
})

DomainShowResult = TypedDict("DomainShowResult", {
    "domain": Any,
    "cnameTarget": str,
    "available": bool,
})

PaymentMethodsListResultItemFieldsItem = TypedDict("PaymentMethodsListResultItemFieldsItem", {
    "name": str,
    "label": str,
    "placeholder": str,
    "required": bool,
    "max": float,
    "secret": bool,
    "showCallback": bool,
    "mode": str,
    "isSet": bool,
    "value": str,
})

PaymentMethodsListResultItemTogglesItem = TypedDict("PaymentMethodsListResultItemTogglesItem", {
    "name": str,
    "label": str,
    "hint": str,
    "group": str,
    "needs": str,
    "on": bool,
})

PaymentMethodsListResultItem = TypedDict("PaymentMethodsListResultItem", {
    "provider": str,
    "name": str,
    "kind": str,
    "blurb": str,
    "tagline": str,
    "accent": str,
    "site": str,
    "callbackUrl": str,
    "returnOrigin": str,
    "originHint": str,
    "callbackHint": str,
    "copies": Union[List[Any], Dict[str, Any]],
    "authorizeUrl": str,
    "connected": bool,
    "enabled": bool,
    "usable": bool,
    "ready": bool,
    "testMode": bool,
    "modes": Union[List[Any], Dict[str, Any]],
    "mode": str,
    "label": str,
    "buyerLabel": str,
    "defaultLabel": str,
    "fields": List[PaymentMethodsListResultItemFieldsItem],
    "toggles": List[PaymentMethodsListResultItemTogglesItem],
    "unpaidHours": Any,
    "updatedAt": Any,
})

PaymentMethodsSetBalanceResultItemFieldsItem = TypedDict("PaymentMethodsSetBalanceResultItemFieldsItem", {
    "name": str,
    "label": str,
    "placeholder": str,
    "required": bool,
    "max": float,
    "secret": bool,
    "showCallback": bool,
    "mode": str,
    "isSet": bool,
    "value": str,
})

PaymentMethodsSetBalanceResultItemTogglesItem = TypedDict("PaymentMethodsSetBalanceResultItemTogglesItem", {
    "name": str,
    "label": str,
    "hint": str,
    "group": str,
    "needs": str,
    "on": bool,
})

PaymentMethodsSetBalanceResultItem = TypedDict("PaymentMethodsSetBalanceResultItem", {
    "provider": str,
    "name": str,
    "kind": str,
    "blurb": str,
    "tagline": str,
    "accent": str,
    "site": str,
    "callbackUrl": str,
    "returnOrigin": str,
    "originHint": str,
    "callbackHint": str,
    "copies": Union[List[Any], Dict[str, Any]],
    "authorizeUrl": str,
    "connected": bool,
    "enabled": bool,
    "usable": bool,
    "ready": bool,
    "testMode": bool,
    "modes": Union[List[Any], Dict[str, Any]],
    "mode": str,
    "label": str,
    "buyerLabel": str,
    "defaultLabel": str,
    "fields": List[PaymentMethodsSetBalanceResultItemFieldsItem],
    "toggles": List[PaymentMethodsSetBalanceResultItemTogglesItem],
    "unpaidHours": Any,
    "updatedAt": Any,
})

PaymentMethodsSetUnpaidHoursResultItemFieldsItem = TypedDict("PaymentMethodsSetUnpaidHoursResultItemFieldsItem", {
    "name": str,
    "label": str,
    "placeholder": str,
    "required": bool,
    "max": float,
    "secret": bool,
    "showCallback": bool,
    "mode": str,
    "isSet": bool,
    "value": str,
})

PaymentMethodsSetUnpaidHoursResultItemTogglesItem = TypedDict("PaymentMethodsSetUnpaidHoursResultItemTogglesItem", {
    "name": str,
    "label": str,
    "hint": str,
    "group": str,
    "needs": str,
    "on": bool,
})

PaymentMethodsSetUnpaidHoursResultItem = TypedDict("PaymentMethodsSetUnpaidHoursResultItem", {
    "provider": str,
    "name": str,
    "kind": str,
    "blurb": str,
    "tagline": str,
    "accent": str,
    "site": str,
    "callbackUrl": str,
    "returnOrigin": str,
    "originHint": str,
    "callbackHint": str,
    "copies": Union[List[Any], Dict[str, Any]],
    "authorizeUrl": str,
    "connected": bool,
    "enabled": bool,
    "usable": bool,
    "ready": bool,
    "testMode": bool,
    "modes": Union[List[Any], Dict[str, Any]],
    "mode": str,
    "label": str,
    "buyerLabel": str,
    "defaultLabel": str,
    "fields": List[PaymentMethodsSetUnpaidHoursResultItemFieldsItem],
    "toggles": List[PaymentMethodsSetUnpaidHoursResultItemTogglesItem],
    "unpaidHours": Any,
    "updatedAt": str,
})

PaymentMethodsSetMethodUnpaidHoursResultItemFieldsItem = TypedDict("PaymentMethodsSetMethodUnpaidHoursResultItemFieldsItem", {
    "name": str,
    "label": str,
    "placeholder": str,
    "required": bool,
    "max": float,
    "secret": bool,
    "showCallback": bool,
    "mode": str,
    "isSet": bool,
    "value": str,
})

PaymentMethodsSetMethodUnpaidHoursResultItemTogglesItem = TypedDict("PaymentMethodsSetMethodUnpaidHoursResultItemTogglesItem", {
    "name": str,
    "label": str,
    "hint": str,
    "group": str,
    "needs": str,
    "on": bool,
})

PaymentMethodsSetMethodUnpaidHoursResultItem = TypedDict("PaymentMethodsSetMethodUnpaidHoursResultItem", {
    "provider": str,
    "name": str,
    "kind": str,
    "blurb": str,
    "tagline": str,
    "accent": str,
    "site": str,
    "callbackUrl": str,
    "returnOrigin": str,
    "originHint": str,
    "callbackHint": str,
    "copies": Union[List[Any], Dict[str, Any]],
    "authorizeUrl": str,
    "connected": bool,
    "enabled": bool,
    "usable": bool,
    "ready": bool,
    "testMode": bool,
    "modes": Union[List[Any], Dict[str, Any]],
    "mode": str,
    "label": str,
    "buyerLabel": str,
    "defaultLabel": str,
    "fields": List[PaymentMethodsSetMethodUnpaidHoursResultItemFieldsItem],
    "toggles": List[PaymentMethodsSetMethodUnpaidHoursResultItemTogglesItem],
    "unpaidHours": float,
    "updatedAt": str,
})

AnalyticsOverviewResultStore = TypedDict("AnalyticsOverviewResultStore", {
    "id": str,
    "name": str,
    "slug": str,
})

AnalyticsOverviewResultRange = TypedDict("AnalyticsOverviewResultRange", {
    "preset": str,
    "from": str,
    "to": str,
    "days": float,
    "timezone": str,
    "inProgress": bool,
})

AnalyticsOverviewResultTotalsRecovered = TypedDict("AnalyticsOverviewResultTotalsRecovered", {
    "revenue": float,
    "orders": float,
})

AnalyticsOverviewResultTotals = TypedDict("AnalyticsOverviewResultTotals", {
    "revenue": float,
    "orders": float,
    "completedOrders": float,
    "newCustomers": float,
    "averageOrderValue": float,
    "visitors": float,
    "conversionRate": float,
    "recovered": AnalyticsOverviewResultTotalsRecovered,
})

AnalyticsOverviewResultPrevious = TypedDict("AnalyticsOverviewResultPrevious", {
    "revenue": float,
    "orders": float,
    "newCustomers": float,
    "averageOrderValue": float,
    "visitors": float,
    "conversionRate": float,
})

AnalyticsOverviewResultChange = TypedDict("AnalyticsOverviewResultChange", {
    "revenue": Any,
    "orders": Any,
    "newCustomers": Any,
    "averageOrderValue": Any,
    "visitors": Any,
    "conversionRate": Any,
})

AnalyticsOverviewResultFunnelItem = TypedDict("AnalyticsOverviewResultFunnelItem", {
    "key": str,
    "count": float,
    "previousCount": float,
    "rate": float,
    "previousRate": float,
    "change": Any,
})

AnalyticsOverviewResultReturningCustomersPrevious = TypedDict("AnalyticsOverviewResultReturningCustomersPrevious", {
    "customers": float,
    "returning": float,
    "rate": float,
})

AnalyticsOverviewResultReturningCustomers = TypedDict("AnalyticsOverviewResultReturningCustomers", {
    "customers": float,
    "returning": float,
    "rate": float,
    "previous": AnalyticsOverviewResultReturningCustomersPrevious,
    "change": Any,
})

AnalyticsOverviewResultSeriesPointsItem = TypedDict("AnalyticsOverviewResultSeriesPointsItem", {
    "at": str,
    "revenue": float,
    "orders": float,
    "previousAt": str,
    "previousRevenue": float,
    "previousOrders": float,
})

AnalyticsOverviewResultSeries = TypedDict("AnalyticsOverviewResultSeries", {
    "bucket": str,
    "points": List[AnalyticsOverviewResultSeriesPointsItem],
})

AnalyticsOverviewResultCustomerSeriesPointsItem = TypedDict("AnalyticsOverviewResultCustomerSeriesPointsItem", {
    "at": str,
    "customers": float,
    "previousAt": str,
    "previousCustomers": float,
})

AnalyticsOverviewResultCustomerSeries = TypedDict("AnalyticsOverviewResultCustomerSeries", {
    "bucket": str,
    "points": List[AnalyticsOverviewResultCustomerSeriesPointsItem],
})

AnalyticsOverviewResultStatusCounts = TypedDict("AnalyticsOverviewResultStatusCounts", {
    "completed": float,
    "pending": float,
    "refunded": float,
    "cancelled": float,
    "chargeback": float,
})

AnalyticsOverviewResultStatusTotalsCompleted = TypedDict("AnalyticsOverviewResultStatusTotalsCompleted", {
    "orders": float,
    "amount": float,
})

AnalyticsOverviewResultStatusTotalsPending = TypedDict("AnalyticsOverviewResultStatusTotalsPending", {
    "orders": float,
    "amount": float,
})

AnalyticsOverviewResultStatusTotalsRefunded = TypedDict("AnalyticsOverviewResultStatusTotalsRefunded", {
    "orders": float,
    "amount": float,
})

AnalyticsOverviewResultStatusTotalsCancelled = TypedDict("AnalyticsOverviewResultStatusTotalsCancelled", {
    "orders": float,
    "amount": float,
})

AnalyticsOverviewResultStatusTotalsChargeback = TypedDict("AnalyticsOverviewResultStatusTotalsChargeback", {
    "orders": float,
    "amount": float,
})

AnalyticsOverviewResultStatusTotals = TypedDict("AnalyticsOverviewResultStatusTotals", {
    "completed": AnalyticsOverviewResultStatusTotalsCompleted,
    "pending": AnalyticsOverviewResultStatusTotalsPending,
    "refunded": AnalyticsOverviewResultStatusTotalsRefunded,
    "cancelled": AnalyticsOverviewResultStatusTotalsCancelled,
    "chargeback": AnalyticsOverviewResultStatusTotalsChargeback,
})

AnalyticsOverviewResultTopCountriesItem = TypedDict("AnalyticsOverviewResultTopCountriesItem", {
    "key": str,
    "orders": float,
    "revenue": float,
    "share": float,
})

AnalyticsOverviewResultTopPaymentMethodsItem = TypedDict("AnalyticsOverviewResultTopPaymentMethodsItem", {
    "key": str,
    "orders": float,
    "revenue": float,
    "share": float,
})

AnalyticsOverviewResultTopProductsItem = TypedDict("AnalyticsOverviewResultTopProductsItem", {
    "productName": str,
    "units": float,
    "orders": float,
    "revenue": float,
})

AnalyticsOverviewResultLifetime = TypedDict("AnalyticsOverviewResultLifetime", {
    "products": float,
    "orders": float,
    "customers": float,
    "categories": float,
})

AnalyticsOverviewResult = TypedDict("AnalyticsOverviewResult", {
    "store": AnalyticsOverviewResultStore,
    "range": AnalyticsOverviewResultRange,
    "currencyCode": str,
    "totals": AnalyticsOverviewResultTotals,
    "previous": AnalyticsOverviewResultPrevious,
    "change": AnalyticsOverviewResultChange,
    "funnel": List[AnalyticsOverviewResultFunnelItem],
    "returningCustomers": AnalyticsOverviewResultReturningCustomers,
    "series": AnalyticsOverviewResultSeries,
    "customerSeries": AnalyticsOverviewResultCustomerSeries,
    "statusCounts": AnalyticsOverviewResultStatusCounts,
    "statusTotals": AnalyticsOverviewResultStatusTotals,
    "week": List[List[float]],
    "topCountries": List[AnalyticsOverviewResultTopCountriesItem],
    "topPaymentMethods": List[AnalyticsOverviewResultTopPaymentMethodsItem],
    "topProducts": List[AnalyticsOverviewResultTopProductsItem],
    "lifetime": AnalyticsOverviewResultLifetime,
})

AnalyticsReportResultStore = TypedDict("AnalyticsReportResultStore", {
    "id": str,
    "name": str,
    "slug": str,
})

AnalyticsReportResultRange = TypedDict("AnalyticsReportResultRange", {
    "preset": str,
    "from": str,
    "to": str,
    "days": float,
    "timezone": str,
    "inProgress": bool,
})

AnalyticsReportResultTotals = TypedDict("AnalyticsReportResultTotals", {
    "sessions": float,
    "visitors": float,
    "pageViews": float,
    "orders": float,
    "revenue": float,
    "visitOrders": float,
    "visitRevenue": float,
    "viewsPerSession": float,
    "avgEngagedSeconds": float,
    "measuredSessions": float,
    "bounceRate": float,
    "cartRate": float,
    "conversionRate": float,
})

AnalyticsReportResultPrevious = TypedDict("AnalyticsReportResultPrevious", {
    "sessions": float,
    "visitors": float,
    "pageViews": float,
    "orders": float,
    "revenue": float,
    "visitOrders": float,
    "visitRevenue": float,
    "viewsPerSession": float,
    "avgEngagedSeconds": float,
    "measuredSessions": float,
    "bounceRate": float,
    "cartRate": float,
    "conversionRate": float,
})

AnalyticsReportResultChange = TypedDict("AnalyticsReportResultChange", {
    "sessions": Any,
    "visitors": Any,
    "pageViews": Any,
    "orders": Any,
    "revenue": Any,
    "visitOrders": Any,
    "visitRevenue": Any,
    "viewsPerSession": Any,
    "avgEngagedSeconds": Any,
    "bounceRate": Any,
    "cartRate": Any,
    "conversionRate": Any,
})

AnalyticsReportResultSeriesPointsItem = TypedDict("AnalyticsReportResultSeriesPointsItem", {
    "at": str,
    "sessions": float,
    "views": float,
    "previousAt": str,
    "previousSessions": float,
    "previousViews": float,
})

AnalyticsReportResultSeries = TypedDict("AnalyticsReportResultSeries", {
    "bucket": str,
    "points": List[AnalyticsReportResultSeriesPointsItem],
})

AnalyticsReportResultPages = TypedDict("AnalyticsReportResultPages", {
    "rows": Union[List[Any], Dict[str, Any]],
    "distinct": float,
    "views": float,
    "coversFrom": str,
    "retentionDays": float,
})

AnalyticsReportResultLanding = TypedDict("AnalyticsReportResultLanding", {
    "rows": Union[List[Any], Dict[str, Any]],
    "distinct": float,
})

AnalyticsReportResultExit = TypedDict("AnalyticsReportResultExit", {
    "rows": Union[List[Any], Dict[str, Any]],
    "distinct": float,
})

AnalyticsReportResultChannels = TypedDict("AnalyticsReportResultChannels", {
    "rows": Union[List[Any], Dict[str, Any]],
    "distinct": float,
})

AnalyticsReportResultReferrers = TypedDict("AnalyticsReportResultReferrers", {
    "rows": Union[List[Any], Dict[str, Any]],
    "distinct": float,
})

AnalyticsReportResultDevices = TypedDict("AnalyticsReportResultDevices", {
    "rows": Union[List[Any], Dict[str, Any]],
    "distinct": float,
})

AnalyticsReportResultBrowsers = TypedDict("AnalyticsReportResultBrowsers", {
    "rows": Union[List[Any], Dict[str, Any]],
    "distinct": float,
})

AnalyticsReportResultSystems = TypedDict("AnalyticsReportResultSystems", {
    "rows": Union[List[Any], Dict[str, Any]],
    "distinct": float,
})

AnalyticsReportResultCampaigns = TypedDict("AnalyticsReportResultCampaigns", {
    "rows": Union[List[Any], Dict[str, Any]],
    "distinct": float,
})

AnalyticsReportResultSources = TypedDict("AnalyticsReportResultSources", {
    "rows": Union[List[Any], Dict[str, Any]],
    "distinct": float,
})

AnalyticsReportResultEngines = TypedDict("AnalyticsReportResultEngines", {
    "rows": Union[List[Any], Dict[str, Any]],
    "sessions": float,
})

AnalyticsReportResultCountries = TypedDict("AnalyticsReportResultCountries", {
    "rows": Union[List[Any], Dict[str, Any]],
    "distinct": float,
})

AnalyticsReportResultCities = TypedDict("AnalyticsReportResultCities", {
    "rows": Union[List[Any], Dict[str, Any]],
})

AnalyticsReportResult = TypedDict("AnalyticsReportResult", {
    "store": AnalyticsReportResultStore,
    "range": AnalyticsReportResultRange,
    "currencyCode": str,
    "totals": AnalyticsReportResultTotals,
    "previous": AnalyticsReportResultPrevious,
    "change": AnalyticsReportResultChange,
    "series": AnalyticsReportResultSeries,
    "pages": AnalyticsReportResultPages,
    "landing": AnalyticsReportResultLanding,
    "exit": AnalyticsReportResultExit,
    "channels": AnalyticsReportResultChannels,
    "referrers": AnalyticsReportResultReferrers,
    "devices": AnalyticsReportResultDevices,
    "browsers": AnalyticsReportResultBrowsers,
    "systems": AnalyticsReportResultSystems,
    "campaigns": AnalyticsReportResultCampaigns,
    "sources": AnalyticsReportResultSources,
    "campaignSales": Union[List[Any], Dict[str, Any]],
    "engines": AnalyticsReportResultEngines,
    "affiliates": Union[List[Any], Dict[str, Any]],
    "countries": AnalyticsReportResultCountries,
    "cities": AnalyticsReportResultCities,
})

AnalyticsLiveResultHome = TypedDict("AnalyticsLiveResultHome", {
    "countryCode": str,
    "country": str,
    "latitude": float,
    "longitude": float,
})

AnalyticsLiveResultNow = TypedDict("AnalyticsLiveResultNow", {
    "visitors": float,
    "carted": float,
    "checkingOut": float,
    "purchased": float,
})

AnalyticsLiveResultToday = TypedDict("AnalyticsLiveResultToday", {
    "sessions": float,
    "views": float,
    "orders": float,
    "revenue": float,
    "from": str,
    "timezone": str,
})

AnalyticsLiveResult = TypedDict("AnalyticsLiveResult", {
    "windowMinutes": float,
    "currencyCode": str,
    "home": AnalyticsLiveResultHome,
    "now": AnalyticsLiveResultNow,
    "today": AnalyticsLiveResultToday,
    "visitors": Union[List[Any], Dict[str, Any]],
    "orders": Union[List[Any], Dict[str, Any]],
    "topPages": Union[List[Any], Dict[str, Any]],
    "topLocations": Union[List[Any], Dict[str, Any]],
})

AnalyticsVisitorsNowResult = TypedDict("AnalyticsVisitorsNowResult", {
    "visitors": float,
    "windowMinutes": float,
})

StorefrontsListResultItem = TypedDict("StorefrontsListResultItem", {
    "id": str,
    "name": str,
    "theme": str,
    "themeVersion": str,
    "published": bool,
    "publishedAt": Any,
    "live": bool,
    "createdAt": str,
    "updatedAt": str,
    "code": bool,
    "engine": str,
    "codeOnCopy": Any,
    "unpublished": bool,
    "accent": Any,
    "headingFont": Any,
    "pages": float,
})

StorefrontsCreateResultItem = TypedDict("StorefrontsCreateResultItem", {
    "id": str,
    "name": str,
    "theme": str,
    "themeVersion": str,
    "published": bool,
    "publishedAt": Any,
    "live": bool,
    "createdAt": str,
    "updatedAt": str,
    "code": bool,
    "engine": str,
    "codeOnCopy": Any,
    "unpublished": bool,
    "accent": Any,
    "headingFont": Any,
    "pages": float,
})

StorefrontsExportResultStorefrontDesignTheme = TypedDict("StorefrontsExportResultStorefrontDesignTheme", {
    "accent": str,
    "accentText": str,
    "page": str,
    "cards": str,
    "text": str,
    "muted": str,
    "border": str,
    "tintArt": bool,
    "headingFont": str,
    "bodyFont": str,
    "headingWeight": str,
    "radius": str,
    "buttonRadius": str,
    "pageWidth": float,
    "motion": bool,
    "customCss": str,
})

StorefrontsExportResultStorefrontDesignAnnouncement = TypedDict("StorefrontsExportResultStorefrontDesignAnnouncement", {
    "enabled": bool,
    "text": str,
    "icon": str,
    "link": str,
    "bg": str,
    "color": str,
    "dismissible": bool,
})

StorefrontsExportResultStorefrontDesignHeaderNavItem = TypedDict("StorefrontsExportResultStorefrontDesignHeaderNavItem", {
    "label": Any,
    "link": Any,
    "icon": Any,
})

StorefrontsExportResultStorefrontDesignHeader = TypedDict("StorefrontsExportResultStorefrontDesignHeader", {
    "showLogo": bool,
    "logo": str,
    "logoSize": float,
    "showName": bool,
    "categoriesMenu": bool,
    "categoriesLabel": str,
    "nav": List[StorefrontsExportResultStorefrontDesignHeaderNavItem],
    "featured": bool,
    "showBlog": bool,
    "showOnline": bool,
    "showSearch": bool,
    "showCart": bool,
    "showAccount": bool,
    "accountLabel": str,
})

StorefrontsExportResultStorefrontDesignFooterColumnsItem = TypedDict("StorefrontsExportResultStorefrontDesignFooterColumnsItem", {
    "title": Any,
    "links": Any,
})

StorefrontsExportResultStorefrontDesignFooter = TypedDict("StorefrontsExportResultStorefrontDesignFooter", {
    "showLogo": bool,
    "showName": bool,
    "tagline": str,
    "about": str,
    "columns": List[StorefrontsExportResultStorefrontDesignFooterColumnsItem],
    "legalTitle": str,
    "policies": bool,
    "privacy": str,
    "help": bool,
    "helpTitle": str,
    "helpText": str,
    "helpLabel": str,
    "helpLink": str,
    "directory": bool,
    "socials": Union[List[Any], Dict[str, Any]],
    "copyright": str,
})

StorefrontsExportResultStorefrontDesignCart = TypedDict("StorefrontsExportResultStorefrontDesignCart", {
    "openOnAdd": bool,
    "bar": bool,
    "showImages": bool,
    "title": str,
    "checkoutLabel": str,
    "note": str,
    "emptyText": str,
    "emptyLinkLabel": str,
    "emptyLink": str,
})

StorefrontsExportResultStorefrontDesignPagesItem = TypedDict("StorefrontsExportResultStorefrontDesignPagesItem", {
    "id": str,
    "kind": str,
    "name": str,
    "path": str,
    "title": str,
    "description": str,
    "hideHeader": bool,
    "hideFooter": bool,
    "sections": List[Any],
})

StorefrontsExportResultStorefrontDesign = TypedDict("StorefrontsExportResultStorefrontDesign", {
    "version": float,
    "theme": StorefrontsExportResultStorefrontDesignTheme,
    "announcement": StorefrontsExportResultStorefrontDesignAnnouncement,
    "header": StorefrontsExportResultStorefrontDesignHeader,
    "footer": StorefrontsExportResultStorefrontDesignFooter,
    "cart": StorefrontsExportResultStorefrontDesignCart,
    "pages": List[StorefrontsExportResultStorefrontDesignPagesItem],
})

StorefrontsExportResultStorefront = TypedDict("StorefrontsExportResultStorefront", {
    "kind": str,
    "format": float,
    "exportedAt": str,
    "name": str,
    "theme": str,
    "design": StorefrontsExportResultStorefrontDesign,
    "files": Any,
})

StorefrontsExportResult = TypedDict("StorefrontsExportResult", {
    "filename": str,
    "storefront": StorefrontsExportResultStorefront,
})

StorefrontsRenameResultItem = TypedDict("StorefrontsRenameResultItem", {
    "id": str,
    "name": str,
    "theme": str,
    "themeVersion": str,
    "published": bool,
    "publishedAt": Any,
    "live": bool,
    "createdAt": str,
    "updatedAt": str,
    "code": bool,
    "engine": str,
    "codeOnCopy": Any,
    "unpublished": bool,
    "accent": Any,
    "headingFont": Any,
    "pages": float,
})

StorefrontsDeleteResultItem = TypedDict("StorefrontsDeleteResultItem", {
    "id": str,
    "name": str,
    "theme": str,
    "themeVersion": str,
    "published": bool,
    "publishedAt": str,
    "live": bool,
    "createdAt": str,
    "updatedAt": str,
    "code": bool,
    "engine": str,
    "codeOnCopy": Any,
    "unpublished": bool,
    "accent": Any,
    "headingFont": Any,
    "pages": float,
})

StorefrontsSetLiveResultItem = TypedDict("StorefrontsSetLiveResultItem", {
    "id": str,
    "name": str,
    "theme": str,
    "themeVersion": str,
    "published": bool,
    "publishedAt": str,
    "live": bool,
    "createdAt": str,
    "updatedAt": str,
    "code": bool,
    "engine": str,
    "codeOnCopy": Any,
    "unpublished": bool,
    "accent": Any,
    "headingFont": Any,
    "pages": float,
})

StorefrontsCodeResultStorefront = TypedDict("StorefrontsCodeResultStorefront", {
    "id": str,
    "name": str,
    "theme": str,
    "themeVersion": str,
    "published": bool,
    "publishedAt": Any,
    "live": bool,
    "createdAt": str,
    "updatedAt": str,
    "code": bool,
    "engine": str,
    "codeOnCopy": Any,
    "unpublished": bool,
    "accent": Any,
    "headingFont": Any,
    "pages": float,
})

StorefrontsCodeResult = TypedDict("StorefrontsCodeResult", {
    "storefront": StorefrontsCodeResultStorefront,
    "theme": str,
    "available": bool,
    "started": bool,
    "version": float,
    "code": Any,
    "versions": Union[List[Any], Dict[str, Any]],
    "preview": Any,
})

StorefrontsCodeStartResultStorefront = TypedDict("StorefrontsCodeStartResultStorefront", {
    "id": str,
    "name": str,
    "theme": str,
    "themeVersion": str,
    "published": bool,
    "publishedAt": Any,
    "live": bool,
    "createdAt": str,
    "updatedAt": str,
    "code": bool,
    "engine": str,
    "codeOnCopy": Any,
    "unpublished": bool,
    "accent": Any,
    "headingFont": Any,
    "pages": float,
})

StorefrontsCodeStartResultCodeFilesItem = TypedDict("StorefrontsCodeStartResultCodeFilesItem", {
    "path": str,
    "hash": str,
    "size": float,
    "added": bool,
    "changed": bool,
    "updatedAt": str,
})

StorefrontsCodeStartResultCodeLimits = TypedDict("StorefrontsCodeStartResultCodeLimits", {
    "files": float,
    "fileBytes": float,
    "bytes": float,
    "used": float,
})

StorefrontsCodeStartResultCodeFolders = TypedDict("StorefrontsCodeStartResultCodeFolders", {
    "layout": List[str],
    "pages": List[str],
    "elements": List[str],
    "parts": List[str],
    "assets": List[str],
    "locales": List[str],
    "config": List[str],
})

StorefrontsCodeStartResultCode = TypedDict("StorefrontsCodeStartResultCode", {
    "rev": float,
    "ahead": float,
    "designAhead": bool,
    "base": str,
    "files": List[StorefrontsCodeStartResultCodeFilesItem],
    "problems": Union[List[Any], Dict[str, Any]],
    "limits": StorefrontsCodeStartResultCodeLimits,
    "folders": StorefrontsCodeStartResultCodeFolders,
})

StorefrontsCodeStartResultPreviewPagesItem = TypedDict("StorefrontsCodeStartResultPreviewPagesItem", {
    "name": str,
    "path": str,
})

StorefrontsCodeStartResultPreview = TypedDict("StorefrontsCodeStartResultPreview", {
    "url": str,
    "param": str,
    "token": str,
    "seconds": float,
    "pages": List[StorefrontsCodeStartResultPreviewPagesItem],
})

StorefrontsCodeStartResult = TypedDict("StorefrontsCodeStartResult", {
    "storefront": StorefrontsCodeStartResultStorefront,
    "theme": str,
    "available": bool,
    "started": bool,
    "version": float,
    "code": StorefrontsCodeStartResultCode,
    "versions": Union[List[Any], Dict[str, Any]],
    "preview": StorefrontsCodeStartResultPreview,
})

StorefrontsCodeFileResult = TypedDict("StorefrontsCodeFileResult", {
    "path": str,
    "hash": str,
    "size": float,
    "added": bool,
    "changed": bool,
    "updatedAt": str,
    "content": str,
})

StorefrontsCodeSaveResultFile = TypedDict("StorefrontsCodeSaveResultFile", {
    "path": str,
    "hash": str,
    "size": float,
    "added": bool,
    "changed": bool,
    "updatedAt": str,
    "content": str,
})

StorefrontsCodeSaveResultCodeFilesItem = TypedDict("StorefrontsCodeSaveResultCodeFilesItem", {
    "path": str,
    "hash": str,
    "size": float,
    "added": bool,
    "changed": bool,
    "updatedAt": str,
})

StorefrontsCodeSaveResultCodeLimits = TypedDict("StorefrontsCodeSaveResultCodeLimits", {
    "files": float,
    "fileBytes": float,
    "bytes": float,
    "used": float,
})

StorefrontsCodeSaveResultCodeFolders = TypedDict("StorefrontsCodeSaveResultCodeFolders", {
    "layout": List[str],
    "pages": List[str],
    "elements": List[str],
    "parts": List[str],
    "assets": List[str],
    "locales": List[str],
    "config": List[str],
})

StorefrontsCodeSaveResultCode = TypedDict("StorefrontsCodeSaveResultCode", {
    "rev": float,
    "ahead": float,
    "designAhead": bool,
    "base": str,
    "files": List[StorefrontsCodeSaveResultCodeFilesItem],
    "problems": Union[List[Any], Dict[str, Any]],
    "limits": StorefrontsCodeSaveResultCodeLimits,
    "folders": StorefrontsCodeSaveResultCodeFolders,
})

StorefrontsCodeSaveResult = TypedDict("StorefrontsCodeSaveResult", {
    "file": StorefrontsCodeSaveResultFile,
    "rev": float,
    "code": StorefrontsCodeSaveResultCode,
})

StorefrontsCodeAddResultFile = TypedDict("StorefrontsCodeAddResultFile", {
    "path": str,
    "hash": str,
    "size": float,
    "added": bool,
    "changed": bool,
    "updatedAt": str,
    "content": str,
})

StorefrontsCodeAddResultCodeFilesItem = TypedDict("StorefrontsCodeAddResultCodeFilesItem", {
    "path": str,
    "hash": str,
    "size": float,
    "added": bool,
    "changed": bool,
    "updatedAt": str,
})

StorefrontsCodeAddResultCodeLimits = TypedDict("StorefrontsCodeAddResultCodeLimits", {
    "files": float,
    "fileBytes": float,
    "bytes": float,
    "used": float,
})

StorefrontsCodeAddResultCodeFolders = TypedDict("StorefrontsCodeAddResultCodeFolders", {
    "layout": List[str],
    "pages": List[str],
    "elements": List[str],
    "parts": List[str],
    "assets": List[str],
    "locales": List[str],
    "config": List[str],
})

StorefrontsCodeAddResultCode = TypedDict("StorefrontsCodeAddResultCode", {
    "rev": float,
    "ahead": float,
    "designAhead": bool,
    "base": str,
    "files": List[StorefrontsCodeAddResultCodeFilesItem],
    "problems": Union[List[Any], Dict[str, Any]],
    "limits": StorefrontsCodeAddResultCodeLimits,
    "folders": StorefrontsCodeAddResultCodeFolders,
})

StorefrontsCodeAddResult = TypedDict("StorefrontsCodeAddResult", {
    "file": StorefrontsCodeAddResultFile,
    "rev": float,
    "code": StorefrontsCodeAddResultCode,
})

StorefrontsCodeDeleteResult = TypedDict("StorefrontsCodeDeleteResult", {
    "rev": float,
})

StorefrontsCodeRenameResultFile = TypedDict("StorefrontsCodeRenameResultFile", {
    "path": str,
    "hash": str,
    "size": float,
    "added": bool,
    "changed": bool,
    "updatedAt": str,
})

StorefrontsCodeRenameResult = TypedDict("StorefrontsCodeRenameResult", {
    "file": StorefrontsCodeRenameResultFile,
    "rev": float,
})

StorefrontsCodePublishResultStorefront = TypedDict("StorefrontsCodePublishResultStorefront", {
    "id": str,
    "name": str,
    "theme": str,
    "themeVersion": str,
    "published": bool,
    "publishedAt": str,
    "live": bool,
    "createdAt": str,
    "updatedAt": str,
    "code": bool,
    "engine": str,
    "codeOnCopy": Any,
    "unpublished": bool,
    "accent": Any,
    "headingFont": Any,
    "pages": float,
})

StorefrontsCodePublishResultCodeFilesItem = TypedDict("StorefrontsCodePublishResultCodeFilesItem", {
    "path": str,
    "hash": str,
    "size": float,
    "added": bool,
    "changed": bool,
    "updatedAt": str,
})

StorefrontsCodePublishResultCodeLimits = TypedDict("StorefrontsCodePublishResultCodeLimits", {
    "files": float,
    "fileBytes": float,
    "bytes": float,
    "used": float,
})

StorefrontsCodePublishResultCodeFolders = TypedDict("StorefrontsCodePublishResultCodeFolders", {
    "layout": List[str],
    "pages": List[str],
    "elements": List[str],
    "parts": List[str],
    "assets": List[str],
    "locales": List[str],
    "config": List[str],
})

StorefrontsCodePublishResultCode = TypedDict("StorefrontsCodePublishResultCode", {
    "rev": float,
    "ahead": float,
    "designAhead": bool,
    "base": str,
    "files": List[StorefrontsCodePublishResultCodeFilesItem],
    "problems": Union[List[Any], Dict[str, Any]],
    "limits": StorefrontsCodePublishResultCodeLimits,
    "folders": StorefrontsCodePublishResultCodeFolders,
})

StorefrontsCodePublishResultVersionsItem = TypedDict("StorefrontsCodePublishResultVersionsItem", {
    "id": str,
    "number": float,
    "live": bool,
    "files": float,
    "createdAt": str,
})

StorefrontsCodePublishResultPreviewPagesItem = TypedDict("StorefrontsCodePublishResultPreviewPagesItem", {
    "name": str,
    "path": str,
})

StorefrontsCodePublishResultPreview = TypedDict("StorefrontsCodePublishResultPreview", {
    "url": str,
    "param": str,
    "token": str,
    "seconds": float,
    "pages": List[StorefrontsCodePublishResultPreviewPagesItem],
})

StorefrontsCodePublishResult = TypedDict("StorefrontsCodePublishResult", {
    "storefront": StorefrontsCodePublishResultStorefront,
    "theme": str,
    "available": bool,
    "started": bool,
    "version": float,
    "code": StorefrontsCodePublishResultCode,
    "versions": List[StorefrontsCodePublishResultVersionsItem],
    "preview": StorefrontsCodePublishResultPreview,
})

RoutingShowResultSettings = TypedDict("RoutingShowResultSettings", {
    "enabled": bool,
    "mode": str,
    "retry": bool,
    "sticky": bool,
    "guard": bool,
    "guardDeclines": float,
    "guardWindow": float,
    "disputeAlert": float,
})

RoutingShowResultProcessorsItem = TypedDict("RoutingShowResultProcessorsItem", {
    "provider": str,
    "name": str,
    "share": float,
    "capMonth": float,
    "capDay": Any,
    "minOrder": Any,
    "maxOrder": Any,
    "state": str,
    "pausedReason": str,
    "pausedAt": Any,
    "month": float,
    "day": float,
    "approved": Any,
    "disputes": Any,
    "fee": Any,
})

RoutingShowResultRulesItem = TypedDict("RoutingShowResultRulesItem", {
    "id": str,
    "kind": str,
    "countries": List[str],
    "amountOp": Any,
    "amount": Any,
    "action": str,
    "provider": str,
})

RoutingShowResultFiguresRouted = TypedDict("RoutingShowResultFiguresRouted", {
    "orders": float,
    "volume": float,
})

RoutingShowResultFiguresSaved = TypedDict("RoutingShowResultFiguresSaved", {
    "orders": float,
    "volume": float,
})

RoutingShowResultFigures = TypedDict("RoutingShowResultFigures", {
    "routed": RoutingShowResultFiguresRouted,
    "approved": Any,
    "saved": RoutingShowResultFiguresSaved,
    "disputes": Any,
})

RoutingShowResultLimits = TypedDict("RoutingShowResultLimits", {
    "rules": float,
    "countries": float,
    "guardWindowMin": float,
    "guardWindowMax": float,
})

RoutingShowResult = TypedDict("RoutingShowResult", {
    "set": bool,
    "settings": RoutingShowResultSettings,
    "processors": List[RoutingShowResultProcessorsItem],
    "rules": List[RoutingShowResultRulesItem],
    "available": Union[List[Any], Dict[str, Any]],
    "figures": RoutingShowResultFigures,
    "limits": RoutingShowResultLimits,
})

RoutingUpdateResultSettings = TypedDict("RoutingUpdateResultSettings", {
    "enabled": bool,
    "mode": str,
    "retry": bool,
    "sticky": bool,
    "guard": bool,
    "guardDeclines": float,
    "guardWindow": float,
    "disputeAlert": float,
})

RoutingUpdateResultProcessorsItem = TypedDict("RoutingUpdateResultProcessorsItem", {
    "provider": str,
    "name": str,
    "share": float,
    "capMonth": float,
    "capDay": Any,
    "minOrder": Any,
    "maxOrder": Any,
    "state": str,
    "pausedReason": str,
    "pausedAt": Any,
    "month": float,
    "day": float,
    "approved": Any,
    "disputes": Any,
    "fee": Any,
})

RoutingUpdateResultRulesItem = TypedDict("RoutingUpdateResultRulesItem", {
    "id": str,
    "kind": str,
    "countries": List[str],
    "amountOp": Any,
    "amount": Any,
    "action": str,
    "provider": str,
})

RoutingUpdateResultFiguresRouted = TypedDict("RoutingUpdateResultFiguresRouted", {
    "orders": float,
    "volume": float,
})

RoutingUpdateResultFiguresSaved = TypedDict("RoutingUpdateResultFiguresSaved", {
    "orders": float,
    "volume": float,
})

RoutingUpdateResultFigures = TypedDict("RoutingUpdateResultFigures", {
    "routed": RoutingUpdateResultFiguresRouted,
    "approved": Any,
    "saved": RoutingUpdateResultFiguresSaved,
    "disputes": Any,
})

RoutingUpdateResultLimits = TypedDict("RoutingUpdateResultLimits", {
    "rules": float,
    "countries": float,
    "guardWindowMin": float,
    "guardWindowMax": float,
})

RoutingUpdateResult = TypedDict("RoutingUpdateResult", {
    "set": bool,
    "settings": RoutingUpdateResultSettings,
    "processors": List[RoutingUpdateResultProcessorsItem],
    "rules": List[RoutingUpdateResultRulesItem],
    "available": Union[List[Any], Dict[str, Any]],
    "figures": RoutingUpdateResultFigures,
    "limits": RoutingUpdateResultLimits,
})

RoutingAddProcessorResultSettings = TypedDict("RoutingAddProcessorResultSettings", {
    "enabled": bool,
    "mode": str,
    "retry": bool,
    "sticky": bool,
    "guard": bool,
    "guardDeclines": float,
    "guardWindow": float,
    "disputeAlert": float,
})

RoutingAddProcessorResultProcessorsItem = TypedDict("RoutingAddProcessorResultProcessorsItem", {
    "provider": str,
    "name": str,
    "share": float,
    "capMonth": Any,
    "capDay": Any,
    "minOrder": Any,
    "maxOrder": Any,
    "state": str,
    "pausedReason": str,
    "pausedAt": Any,
    "month": float,
    "day": float,
    "approved": Any,
    "disputes": Any,
    "fee": Any,
})

RoutingAddProcessorResultAvailableItem = TypedDict("RoutingAddProcessorResultAvailableItem", {
    "provider": str,
    "name": str,
    "usable": bool,
})

RoutingAddProcessorResultFiguresRouted = TypedDict("RoutingAddProcessorResultFiguresRouted", {
    "orders": float,
    "volume": float,
})

RoutingAddProcessorResultFiguresSaved = TypedDict("RoutingAddProcessorResultFiguresSaved", {
    "orders": float,
    "volume": float,
})

RoutingAddProcessorResultFigures = TypedDict("RoutingAddProcessorResultFigures", {
    "routed": RoutingAddProcessorResultFiguresRouted,
    "approved": Any,
    "saved": RoutingAddProcessorResultFiguresSaved,
    "disputes": Any,
})

RoutingAddProcessorResultLimits = TypedDict("RoutingAddProcessorResultLimits", {
    "rules": float,
    "countries": float,
    "guardWindowMin": float,
    "guardWindowMax": float,
})

RoutingAddProcessorResult = TypedDict("RoutingAddProcessorResult", {
    "set": bool,
    "settings": RoutingAddProcessorResultSettings,
    "processors": List[RoutingAddProcessorResultProcessorsItem],
    "rules": Union[List[Any], Dict[str, Any]],
    "available": List[RoutingAddProcessorResultAvailableItem],
    "figures": RoutingAddProcessorResultFigures,
    "limits": RoutingAddProcessorResultLimits,
})

RoutingUpdateProcessorResultSettings = TypedDict("RoutingUpdateProcessorResultSettings", {
    "enabled": bool,
    "mode": str,
    "retry": bool,
    "sticky": bool,
    "guard": bool,
    "guardDeclines": float,
    "guardWindow": float,
    "disputeAlert": float,
})

RoutingUpdateProcessorResultProcessorsItem = TypedDict("RoutingUpdateProcessorResultProcessorsItem", {
    "provider": str,
    "name": str,
    "share": float,
    "capMonth": float,
    "capDay": Any,
    "minOrder": Any,
    "maxOrder": Any,
    "state": str,
    "pausedReason": str,
    "pausedAt": Any,
    "month": float,
    "day": float,
    "approved": Any,
    "disputes": Any,
    "fee": Any,
})

RoutingUpdateProcessorResultFiguresRouted = TypedDict("RoutingUpdateProcessorResultFiguresRouted", {
    "orders": float,
    "volume": float,
})

RoutingUpdateProcessorResultFiguresSaved = TypedDict("RoutingUpdateProcessorResultFiguresSaved", {
    "orders": float,
    "volume": float,
})

RoutingUpdateProcessorResultFigures = TypedDict("RoutingUpdateProcessorResultFigures", {
    "routed": RoutingUpdateProcessorResultFiguresRouted,
    "approved": Any,
    "saved": RoutingUpdateProcessorResultFiguresSaved,
    "disputes": Any,
})

RoutingUpdateProcessorResultLimits = TypedDict("RoutingUpdateProcessorResultLimits", {
    "rules": float,
    "countries": float,
    "guardWindowMin": float,
    "guardWindowMax": float,
})

RoutingUpdateProcessorResult = TypedDict("RoutingUpdateProcessorResult", {
    "set": bool,
    "settings": RoutingUpdateProcessorResultSettings,
    "processors": List[RoutingUpdateProcessorResultProcessorsItem],
    "rules": Union[List[Any], Dict[str, Any]],
    "available": Union[List[Any], Dict[str, Any]],
    "figures": RoutingUpdateProcessorResultFigures,
    "limits": RoutingUpdateProcessorResultLimits,
})

RoutingRemoveProcessorResultSettings = TypedDict("RoutingRemoveProcessorResultSettings", {
    "enabled": bool,
    "mode": str,
    "retry": bool,
    "sticky": bool,
    "guard": bool,
    "guardDeclines": float,
    "guardWindow": float,
    "disputeAlert": float,
})

RoutingRemoveProcessorResultProcessorsItem = TypedDict("RoutingRemoveProcessorResultProcessorsItem", {
    "provider": str,
    "name": str,
    "share": float,
    "capMonth": float,
    "capDay": Any,
    "minOrder": Any,
    "maxOrder": Any,
    "state": str,
    "pausedReason": str,
    "pausedAt": Any,
    "month": float,
    "day": float,
    "approved": Any,
    "disputes": Any,
    "fee": Any,
})

RoutingRemoveProcessorResultAvailableItem = TypedDict("RoutingRemoveProcessorResultAvailableItem", {
    "provider": str,
    "name": str,
    "usable": bool,
})

RoutingRemoveProcessorResultFiguresRouted = TypedDict("RoutingRemoveProcessorResultFiguresRouted", {
    "orders": float,
    "volume": float,
})

RoutingRemoveProcessorResultFiguresSaved = TypedDict("RoutingRemoveProcessorResultFiguresSaved", {
    "orders": float,
    "volume": float,
})

RoutingRemoveProcessorResultFigures = TypedDict("RoutingRemoveProcessorResultFigures", {
    "routed": RoutingRemoveProcessorResultFiguresRouted,
    "approved": Any,
    "saved": RoutingRemoveProcessorResultFiguresSaved,
    "disputes": Any,
})

RoutingRemoveProcessorResultLimits = TypedDict("RoutingRemoveProcessorResultLimits", {
    "rules": float,
    "countries": float,
    "guardWindowMin": float,
    "guardWindowMax": float,
})

RoutingRemoveProcessorResult = TypedDict("RoutingRemoveProcessorResult", {
    "set": bool,
    "settings": RoutingRemoveProcessorResultSettings,
    "processors": List[RoutingRemoveProcessorResultProcessorsItem],
    "rules": Union[List[Any], Dict[str, Any]],
    "available": List[RoutingRemoveProcessorResultAvailableItem],
    "figures": RoutingRemoveProcessorResultFigures,
    "limits": RoutingRemoveProcessorResultLimits,
})

RoutingResumeProcessorResultSettings = TypedDict("RoutingResumeProcessorResultSettings", {
    "enabled": bool,
    "mode": str,
    "retry": bool,
    "sticky": bool,
    "guard": bool,
    "guardDeclines": float,
    "guardWindow": float,
    "disputeAlert": float,
})

RoutingResumeProcessorResultProcessorsItem = TypedDict("RoutingResumeProcessorResultProcessorsItem", {
    "provider": str,
    "name": str,
    "share": float,
    "capMonth": float,
    "capDay": Any,
    "minOrder": Any,
    "maxOrder": Any,
    "state": str,
    "pausedReason": str,
    "pausedAt": Any,
    "month": float,
    "day": float,
    "approved": Any,
    "disputes": Any,
    "fee": Any,
})

RoutingResumeProcessorResultRulesItem = TypedDict("RoutingResumeProcessorResultRulesItem", {
    "id": str,
    "kind": str,
    "countries": List[str],
    "amountOp": Any,
    "amount": Any,
    "action": str,
    "provider": str,
})

RoutingResumeProcessorResultFiguresRouted = TypedDict("RoutingResumeProcessorResultFiguresRouted", {
    "orders": float,
    "volume": float,
})

RoutingResumeProcessorResultFiguresSaved = TypedDict("RoutingResumeProcessorResultFiguresSaved", {
    "orders": float,
    "volume": float,
})

RoutingResumeProcessorResultFigures = TypedDict("RoutingResumeProcessorResultFigures", {
    "routed": RoutingResumeProcessorResultFiguresRouted,
    "approved": Any,
    "saved": RoutingResumeProcessorResultFiguresSaved,
    "disputes": Any,
})

RoutingResumeProcessorResultLimits = TypedDict("RoutingResumeProcessorResultLimits", {
    "rules": float,
    "countries": float,
    "guardWindowMin": float,
    "guardWindowMax": float,
})

RoutingResumeProcessorResult = TypedDict("RoutingResumeProcessorResult", {
    "set": bool,
    "settings": RoutingResumeProcessorResultSettings,
    "processors": List[RoutingResumeProcessorResultProcessorsItem],
    "rules": List[RoutingResumeProcessorResultRulesItem],
    "available": Union[List[Any], Dict[str, Any]],
    "figures": RoutingResumeProcessorResultFigures,
    "limits": RoutingResumeProcessorResultLimits,
})

RoutingSortProcessorsResultSettings = TypedDict("RoutingSortProcessorsResultSettings", {
    "enabled": bool,
    "mode": str,
    "retry": bool,
    "sticky": bool,
    "guard": bool,
    "guardDeclines": float,
    "guardWindow": float,
    "disputeAlert": float,
})

RoutingSortProcessorsResultProcessorsItem = TypedDict("RoutingSortProcessorsResultProcessorsItem", {
    "provider": str,
    "name": str,
    "share": float,
    "capMonth": float,
    "capDay": Any,
    "minOrder": Any,
    "maxOrder": Any,
    "state": str,
    "pausedReason": str,
    "pausedAt": Any,
    "month": float,
    "day": float,
    "approved": Any,
    "disputes": Any,
    "fee": Any,
})

RoutingSortProcessorsResultFiguresRouted = TypedDict("RoutingSortProcessorsResultFiguresRouted", {
    "orders": float,
    "volume": float,
})

RoutingSortProcessorsResultFiguresSaved = TypedDict("RoutingSortProcessorsResultFiguresSaved", {
    "orders": float,
    "volume": float,
})

RoutingSortProcessorsResultFigures = TypedDict("RoutingSortProcessorsResultFigures", {
    "routed": RoutingSortProcessorsResultFiguresRouted,
    "approved": Any,
    "saved": RoutingSortProcessorsResultFiguresSaved,
    "disputes": Any,
})

RoutingSortProcessorsResultLimits = TypedDict("RoutingSortProcessorsResultLimits", {
    "rules": float,
    "countries": float,
    "guardWindowMin": float,
    "guardWindowMax": float,
})

RoutingSortProcessorsResult = TypedDict("RoutingSortProcessorsResult", {
    "set": bool,
    "settings": RoutingSortProcessorsResultSettings,
    "processors": List[RoutingSortProcessorsResultProcessorsItem],
    "rules": Union[List[Any], Dict[str, Any]],
    "available": Union[List[Any], Dict[str, Any]],
    "figures": RoutingSortProcessorsResultFigures,
    "limits": RoutingSortProcessorsResultLimits,
})

RoutingAddRuleResultSettings = TypedDict("RoutingAddRuleResultSettings", {
    "enabled": bool,
    "mode": str,
    "retry": bool,
    "sticky": bool,
    "guard": bool,
    "guardDeclines": float,
    "guardWindow": float,
    "disputeAlert": float,
})

RoutingAddRuleResultProcessorsItem = TypedDict("RoutingAddRuleResultProcessorsItem", {
    "provider": str,
    "name": str,
    "share": float,
    "capMonth": float,
    "capDay": Any,
    "minOrder": Any,
    "maxOrder": Any,
    "state": str,
    "pausedReason": str,
    "pausedAt": Any,
    "month": float,
    "day": float,
    "approved": Any,
    "disputes": Any,
    "fee": Any,
})

RoutingAddRuleResultRulesItem = TypedDict("RoutingAddRuleResultRulesItem", {
    "id": str,
    "kind": str,
    "countries": Union[List[Any], Dict[str, Any]],
    "amountOp": str,
    "amount": float,
    "action": str,
    "provider": str,
})

RoutingAddRuleResultFiguresRouted = TypedDict("RoutingAddRuleResultFiguresRouted", {
    "orders": float,
    "volume": float,
})

RoutingAddRuleResultFiguresSaved = TypedDict("RoutingAddRuleResultFiguresSaved", {
    "orders": float,
    "volume": float,
})

RoutingAddRuleResultFigures = TypedDict("RoutingAddRuleResultFigures", {
    "routed": RoutingAddRuleResultFiguresRouted,
    "approved": Any,
    "saved": RoutingAddRuleResultFiguresSaved,
    "disputes": Any,
})

RoutingAddRuleResultLimits = TypedDict("RoutingAddRuleResultLimits", {
    "rules": float,
    "countries": float,
    "guardWindowMin": float,
    "guardWindowMax": float,
})

RoutingAddRuleResult = TypedDict("RoutingAddRuleResult", {
    "set": bool,
    "settings": RoutingAddRuleResultSettings,
    "processors": List[RoutingAddRuleResultProcessorsItem],
    "rules": List[RoutingAddRuleResultRulesItem],
    "available": Union[List[Any], Dict[str, Any]],
    "figures": RoutingAddRuleResultFigures,
    "limits": RoutingAddRuleResultLimits,
})

RoutingUpdateRuleResultSettings = TypedDict("RoutingUpdateRuleResultSettings", {
    "enabled": bool,
    "mode": str,
    "retry": bool,
    "sticky": bool,
    "guard": bool,
    "guardDeclines": float,
    "guardWindow": float,
    "disputeAlert": float,
})

RoutingUpdateRuleResultProcessorsItem = TypedDict("RoutingUpdateRuleResultProcessorsItem", {
    "provider": str,
    "name": str,
    "share": float,
    "capMonth": float,
    "capDay": Any,
    "minOrder": Any,
    "maxOrder": Any,
    "state": str,
    "pausedReason": str,
    "pausedAt": Any,
    "month": float,
    "day": float,
    "approved": Any,
    "disputes": Any,
    "fee": Any,
})

RoutingUpdateRuleResultRulesItem = TypedDict("RoutingUpdateRuleResultRulesItem", {
    "id": str,
    "kind": str,
    "countries": List[str],
    "amountOp": Any,
    "amount": Any,
    "action": str,
    "provider": str,
})

RoutingUpdateRuleResultFiguresRouted = TypedDict("RoutingUpdateRuleResultFiguresRouted", {
    "orders": float,
    "volume": float,
})

RoutingUpdateRuleResultFiguresSaved = TypedDict("RoutingUpdateRuleResultFiguresSaved", {
    "orders": float,
    "volume": float,
})

RoutingUpdateRuleResultFigures = TypedDict("RoutingUpdateRuleResultFigures", {
    "routed": RoutingUpdateRuleResultFiguresRouted,
    "approved": Any,
    "saved": RoutingUpdateRuleResultFiguresSaved,
    "disputes": Any,
})

RoutingUpdateRuleResultLimits = TypedDict("RoutingUpdateRuleResultLimits", {
    "rules": float,
    "countries": float,
    "guardWindowMin": float,
    "guardWindowMax": float,
})

RoutingUpdateRuleResult = TypedDict("RoutingUpdateRuleResult", {
    "set": bool,
    "settings": RoutingUpdateRuleResultSettings,
    "processors": List[RoutingUpdateRuleResultProcessorsItem],
    "rules": List[RoutingUpdateRuleResultRulesItem],
    "available": Union[List[Any], Dict[str, Any]],
    "figures": RoutingUpdateRuleResultFigures,
    "limits": RoutingUpdateRuleResultLimits,
})

RoutingDeleteRuleResultSettings = TypedDict("RoutingDeleteRuleResultSettings", {
    "enabled": bool,
    "mode": str,
    "retry": bool,
    "sticky": bool,
    "guard": bool,
    "guardDeclines": float,
    "guardWindow": float,
    "disputeAlert": float,
})

RoutingDeleteRuleResultProcessorsItem = TypedDict("RoutingDeleteRuleResultProcessorsItem", {
    "provider": str,
    "name": str,
    "share": float,
    "capMonth": float,
    "capDay": Any,
    "minOrder": Any,
    "maxOrder": Any,
    "state": str,
    "pausedReason": str,
    "pausedAt": Any,
    "month": float,
    "day": float,
    "approved": Any,
    "disputes": Any,
    "fee": Any,
})

RoutingDeleteRuleResultFiguresRouted = TypedDict("RoutingDeleteRuleResultFiguresRouted", {
    "orders": float,
    "volume": float,
})

RoutingDeleteRuleResultFiguresSaved = TypedDict("RoutingDeleteRuleResultFiguresSaved", {
    "orders": float,
    "volume": float,
})

RoutingDeleteRuleResultFigures = TypedDict("RoutingDeleteRuleResultFigures", {
    "routed": RoutingDeleteRuleResultFiguresRouted,
    "approved": Any,
    "saved": RoutingDeleteRuleResultFiguresSaved,
    "disputes": Any,
})

RoutingDeleteRuleResultLimits = TypedDict("RoutingDeleteRuleResultLimits", {
    "rules": float,
    "countries": float,
    "guardWindowMin": float,
    "guardWindowMax": float,
})

RoutingDeleteRuleResult = TypedDict("RoutingDeleteRuleResult", {
    "set": bool,
    "settings": RoutingDeleteRuleResultSettings,
    "processors": List[RoutingDeleteRuleResultProcessorsItem],
    "rules": Union[List[Any], Dict[str, Any]],
    "available": Union[List[Any], Dict[str, Any]],
    "figures": RoutingDeleteRuleResultFigures,
    "limits": RoutingDeleteRuleResultLimits,
})

RoutingSortRulesResultSettings = TypedDict("RoutingSortRulesResultSettings", {
    "enabled": bool,
    "mode": str,
    "retry": bool,
    "sticky": bool,
    "guard": bool,
    "guardDeclines": float,
    "guardWindow": float,
    "disputeAlert": float,
})

RoutingSortRulesResultProcessorsItem = TypedDict("RoutingSortRulesResultProcessorsItem", {
    "provider": str,
    "name": str,
    "share": float,
    "capMonth": float,
    "capDay": Any,
    "minOrder": Any,
    "maxOrder": Any,
    "state": str,
    "pausedReason": str,
    "pausedAt": Any,
    "month": float,
    "day": float,
    "approved": Any,
    "disputes": Any,
    "fee": Any,
})

RoutingSortRulesResultRulesItem = TypedDict("RoutingSortRulesResultRulesItem", {
    "id": str,
    "kind": str,
    "countries": List[str],
    "amountOp": Any,
    "amount": Any,
    "action": str,
    "provider": str,
})

RoutingSortRulesResultFiguresRouted = TypedDict("RoutingSortRulesResultFiguresRouted", {
    "orders": float,
    "volume": float,
})

RoutingSortRulesResultFiguresSaved = TypedDict("RoutingSortRulesResultFiguresSaved", {
    "orders": float,
    "volume": float,
})

RoutingSortRulesResultFigures = TypedDict("RoutingSortRulesResultFigures", {
    "routed": RoutingSortRulesResultFiguresRouted,
    "approved": Any,
    "saved": RoutingSortRulesResultFiguresSaved,
    "disputes": Any,
})

RoutingSortRulesResultLimits = TypedDict("RoutingSortRulesResultLimits", {
    "rules": float,
    "countries": float,
    "guardWindowMin": float,
    "guardWindowMax": float,
})

RoutingSortRulesResult = TypedDict("RoutingSortRulesResult", {
    "set": bool,
    "settings": RoutingSortRulesResultSettings,
    "processors": List[RoutingSortRulesResultProcessorsItem],
    "rules": List[RoutingSortRulesResultRulesItem],
    "available": Union[List[Any], Dict[str, Any]],
    "figures": RoutingSortRulesResultFigures,
    "limits": RoutingSortRulesResultLimits,
})

CustomMethodsListResultItem = TypedDict("CustomMethodsListResultItem", {
    "id": str,
    "kind": str,
    "name": str,
    "description": str,
    "instructions": str,
    "redirectUrl": str,
    "iconUrl": Any,
    "asksProof": bool,
    "requiresPicture": bool,
    "enabled": bool,
})

CustomMethodsCreateResult = TypedDict("CustomMethodsCreateResult", {
    "id": str,
    "kind": str,
    "name": str,
    "description": str,
    "instructions": str,
    "redirectUrl": str,
    "iconUrl": Any,
    "asksProof": bool,
    "requiresPicture": bool,
    "enabled": bool,
})

CustomMethodsUpdateResultItem = TypedDict("CustomMethodsUpdateResultItem", {
    "id": str,
    "kind": str,
    "name": str,
    "description": str,
    "instructions": str,
    "redirectUrl": str,
    "iconUrl": Any,
    "asksProof": bool,
    "requiresPicture": bool,
    "enabled": bool,
})

CustomMethodsDeleteResultItem = TypedDict("CustomMethodsDeleteResultItem", {
    "id": str,
    "kind": str,
    "name": str,
    "description": str,
    "instructions": str,
    "redirectUrl": str,
    "iconUrl": Any,
    "asksProof": bool,
    "requiresPicture": bool,
    "enabled": bool,
})

CustomMethodsSetEnabledResultItem = TypedDict("CustomMethodsSetEnabledResultItem", {
    "id": str,
    "kind": str,
    "name": str,
    "description": str,
    "instructions": str,
    "redirectUrl": str,
    "iconUrl": Any,
    "asksProof": bool,
    "requiresPicture": bool,
    "enabled": bool,
})

CustomMethodsSortResultItem = TypedDict("CustomMethodsSortResultItem", {
    "id": str,
    "kind": str,
    "name": str,
    "description": str,
    "instructions": str,
    "redirectUrl": str,
    "iconUrl": Any,
    "asksProof": bool,
    "requiresPicture": bool,
    "enabled": bool,
})

ProductsListResultItemBadgesItem = TypedDict("ProductsListResultItemBadgesItem", {
    "label": str,
    "color": str,
    "kind": str,
})

ProductsListResultItemFeaturesItem = TypedDict("ProductsListResultItemFeaturesItem", {
    "type": str,
    "name": str,
})

ProductsListResultItemVariantsItem = TypedDict("ProductsListResultItemVariantsItem", {
    "id": str,
    "label": str,
    "price": float,
    "duration": str,
    "durationDays": float,
    "stockMode": float,
    "minQuantity": float,
    "maxQuantity": float,
    "stock": float,
    "keyCount": float,
    "deliveryMethods": List[str],
    "deliveryType": str,
    "deliveryInstructions": str,
    "dynamicUrl": str,
    "customFieldsOn": bool,
    "customFields": Union[List[Any], Dict[str, Any]],
    "sort": float,
    "blockedPaymentMethods": Union[List[Any], Dict[str, Any]],
})

ProductsListResultItem = TypedDict("ProductsListResultItem", {
    "id": str,
    "storeId": str,
    "name": str,
    "slug": str,
    "description": str,
    "seoTitle": str,
    "seoDescription": str,
    "image": str,
    "imageUrl": Any,
    "visibility": str,
    "sort": float,
    "isBestSeller": bool,
    "badges": List[ProductsListResultItemBadgesItem],
    "features": List[ProductsListResultItemFeaturesItem],
    "deliveryInstructions": str,
    "blockedPaymentMethods": Union[List[Any], Dict[str, Any]],
    "paymentFees": Union[List[Any], Dict[str, Any]],
    "showViewers": bool,
    "showSales": bool,
    "salesWindow": str,
    "saleNotifications": bool,
    "metadata": str,
    "dateCreated": str,
    "updatedAt": str,
    "categoryIds": List[str],
    "unitsSold": float,
    "revenue": float,
    "lowPrice": float,
    "highPrice": float,
    "totalStock": float,
    "untrackedVariants": float,
    "imageCount": float,
    "images": Union[List[Any], Dict[str, Any]],
    "variants": List[ProductsListResultItemVariantsItem],
    "runningSubscriptions": float,
})

ProductsCreateResultBadgesItem = TypedDict("ProductsCreateResultBadgesItem", {
    "label": str,
    "color": str,
    "kind": str,
})

ProductsCreateResultFeaturesItem = TypedDict("ProductsCreateResultFeaturesItem", {
    "type": str,
    "name": str,
})

ProductsCreateResultVariantsItem = TypedDict("ProductsCreateResultVariantsItem", {
    "id": str,
    "label": str,
    "price": float,
    "duration": str,
    "durationDays": float,
    "stockMode": float,
    "minQuantity": float,
    "maxQuantity": float,
    "stock": float,
    "keyCount": float,
    "deliveryMethods": List[str],
    "deliveryType": str,
    "deliveryInstructions": str,
    "dynamicUrl": str,
    "customFieldsOn": bool,
    "customFields": Union[List[Any], Dict[str, Any]],
    "sort": float,
    "blockedPaymentMethods": Union[List[Any], Dict[str, Any]],
})

ProductsCreateResult = TypedDict("ProductsCreateResult", {
    "id": str,
    "storeId": str,
    "name": str,
    "slug": str,
    "description": str,
    "seoTitle": str,
    "seoDescription": str,
    "image": str,
    "imageUrl": Any,
    "visibility": str,
    "sort": float,
    "isBestSeller": bool,
    "badges": List[ProductsCreateResultBadgesItem],
    "features": List[ProductsCreateResultFeaturesItem],
    "deliveryInstructions": str,
    "blockedPaymentMethods": Union[List[Any], Dict[str, Any]],
    "paymentFees": Union[List[Any], Dict[str, Any]],
    "showViewers": bool,
    "showSales": bool,
    "salesWindow": str,
    "saleNotifications": bool,
    "metadata": str,
    "dateCreated": str,
    "updatedAt": str,
    "categoryIds": List[str],
    "unitsSold": float,
    "revenue": float,
    "lowPrice": float,
    "highPrice": float,
    "totalStock": float,
    "untrackedVariants": float,
    "imageCount": float,
    "images": Union[List[Any], Dict[str, Any]],
    "variants": List[ProductsCreateResultVariantsItem],
    "runningSubscriptions": float,
})

ProductsShowResultBadgesItem = TypedDict("ProductsShowResultBadgesItem", {
    "label": str,
    "color": str,
    "kind": str,
})

ProductsShowResultFeaturesItem = TypedDict("ProductsShowResultFeaturesItem", {
    "type": str,
    "name": str,
})

ProductsShowResultVariantsItem = TypedDict("ProductsShowResultVariantsItem", {
    "id": str,
    "label": str,
    "price": float,
    "duration": str,
    "durationDays": float,
    "stockMode": float,
    "minQuantity": float,
    "maxQuantity": float,
    "stock": float,
    "keyCount": float,
    "deliveryMethods": List[str],
    "deliveryType": str,
    "deliveryInstructions": str,
    "dynamicUrl": str,
    "customFieldsOn": bool,
    "customFields": Union[List[Any], Dict[str, Any]],
    "sort": float,
    "blockedPaymentMethods": Union[List[Any], Dict[str, Any]],
})

ProductsShowResult = TypedDict("ProductsShowResult", {
    "id": str,
    "storeId": str,
    "name": str,
    "slug": str,
    "description": str,
    "seoTitle": str,
    "seoDescription": str,
    "image": str,
    "imageUrl": Any,
    "visibility": str,
    "sort": float,
    "isBestSeller": bool,
    "badges": List[ProductsShowResultBadgesItem],
    "features": List[ProductsShowResultFeaturesItem],
    "deliveryInstructions": str,
    "blockedPaymentMethods": Union[List[Any], Dict[str, Any]],
    "paymentFees": Union[List[Any], Dict[str, Any]],
    "showViewers": bool,
    "showSales": bool,
    "salesWindow": str,
    "saleNotifications": bool,
    "metadata": str,
    "dateCreated": str,
    "updatedAt": str,
    "categoryIds": List[str],
    "unitsSold": float,
    "revenue": float,
    "lowPrice": float,
    "highPrice": float,
    "totalStock": float,
    "untrackedVariants": float,
    "imageCount": float,
    "images": Union[List[Any], Dict[str, Any]],
    "variants": List[ProductsShowResultVariantsItem],
    "runningSubscriptions": float,
})

ProductsUpdateResultBadgesItem = TypedDict("ProductsUpdateResultBadgesItem", {
    "label": str,
    "color": str,
    "kind": str,
})

ProductsUpdateResultFeaturesItem = TypedDict("ProductsUpdateResultFeaturesItem", {
    "type": str,
    "name": str,
})

ProductsUpdateResultVariantsItem = TypedDict("ProductsUpdateResultVariantsItem", {
    "id": str,
    "label": str,
    "price": float,
    "duration": str,
    "durationDays": float,
    "stockMode": float,
    "minQuantity": float,
    "maxQuantity": float,
    "stock": float,
    "keyCount": float,
    "deliveryMethods": List[str],
    "deliveryType": str,
    "deliveryInstructions": str,
    "dynamicUrl": str,
    "customFieldsOn": bool,
    "customFields": Union[List[Any], Dict[str, Any]],
    "sort": float,
    "blockedPaymentMethods": Union[List[Any], Dict[str, Any]],
})

ProductsUpdateResult = TypedDict("ProductsUpdateResult", {
    "id": str,
    "storeId": str,
    "name": str,
    "slug": str,
    "description": str,
    "seoTitle": str,
    "seoDescription": str,
    "image": str,
    "imageUrl": Any,
    "visibility": str,
    "sort": float,
    "isBestSeller": bool,
    "badges": List[ProductsUpdateResultBadgesItem],
    "features": List[ProductsUpdateResultFeaturesItem],
    "deliveryInstructions": str,
    "blockedPaymentMethods": Union[List[Any], Dict[str, Any]],
    "paymentFees": Union[List[Any], Dict[str, Any]],
    "showViewers": bool,
    "showSales": bool,
    "salesWindow": str,
    "saleNotifications": bool,
    "metadata": str,
    "dateCreated": str,
    "updatedAt": str,
    "categoryIds": List[str],
    "unitsSold": float,
    "revenue": float,
    "lowPrice": float,
    "highPrice": float,
    "totalStock": float,
    "untrackedVariants": float,
    "imageCount": float,
    "images": Union[List[Any], Dict[str, Any]],
    "variants": List[ProductsUpdateResultVariantsItem],
    "runningSubscriptions": float,
})

ProductsSetVisibilityResult = TypedDict("ProductsSetVisibilityResult", {
    "id": str,
    "visibility": str,
})

ProductsSortResult = TypedDict("ProductsSortResult", {
    "reordered": float,
})

ProductsBulkUpdateResult = TypedDict("ProductsBulkUpdateResult", {
    "updated": float,
})

StockListKeysItem = TypedDict("StockListKeysItem", {
    "id": str,
    "value": str,
})

StockAddKeysResult = TypedDict("StockAddKeysResult", {
    "added": float,
    "skipped": float,
    "duplicates": float,
    "available": float,
})

StockDeleteKeysResult = TypedDict("StockDeleteKeysResult", {
    "removed": float,
    "available": float,
})

CategoriesListResultItem = TypedDict("CategoriesListResultItem", {
    "id": str,
    "storeId": str,
    "name": str,
    "slug": str,
    "visibility": str,
    "isPopular": bool,
    "description": str,
    "seoTitle": str,
    "seoDescription": str,
    "image": str,
    "imageUrl": Any,
    "sort": float,
    "productIds": List[str],
    "productCount": float,
    "dateCreated": str,
    "updatedAt": str,
})

CategoriesCreateResult = TypedDict("CategoriesCreateResult", {
    "id": str,
    "storeId": str,
    "name": str,
    "slug": str,
    "visibility": str,
    "isPopular": bool,
    "description": str,
    "seoTitle": str,
    "seoDescription": str,
    "image": str,
    "imageUrl": Any,
    "sort": float,
    "productIds": Union[List[Any], Dict[str, Any]],
    "productCount": float,
    "dateCreated": str,
    "updatedAt": str,
})

CategoriesUpdateResult = TypedDict("CategoriesUpdateResult", {
    "id": str,
    "storeId": str,
    "name": str,
    "slug": str,
    "visibility": str,
    "isPopular": bool,
    "description": str,
    "seoTitle": str,
    "seoDescription": str,
    "image": str,
    "imageUrl": Any,
    "sort": float,
    "productIds": List[str],
    "productCount": float,
    "dateCreated": str,
    "updatedAt": str,
})

CategoriesDeleteResult = TypedDict("CategoriesDeleteResult", {
    "id": str,
    "deleted": bool,
})

CategoriesSortResult = TypedDict("CategoriesSortResult", {
    "reordered": float,
})

UpsellsListResultItemTargetsItem = TypedDict("UpsellsListResultItemTargetsItem", {
    "type": str,
    "id": str,
    "name": str,
})

UpsellsListResultItem = TypedDict("UpsellsListResultItem", {
    "id": str,
    "kind": str,
    "name": str,
    "enabled": bool,
    "sells": str,
    "productId": Any,
    "variantId": Any,
    "productName": Any,
    "productImage": Any,
    "variantLabel": Any,
    "variantPrice": Any,
    "price": float,
    "cost": Any,
    "message": str,
    "offered": str,
    "charged": str,
    "trigger": str,
    "minSubtotal": Any,
    "discountType": str,
    "discountValue": float,
    "words": str,
    "startsAt": Any,
    "endsAt": Any,
    "firstOrders": bool,
    "hideOwned": bool,
    "targets": List[UpsellsListResultItemTargetsItem],
    "shown": float,
    "taken": float,
    "revenue": float,
    "dateCreated": str,
    "updatedAt": str,
})

UpsellsCreateResultTargetsItem = TypedDict("UpsellsCreateResultTargetsItem", {
    "type": str,
    "id": str,
    "name": str,
})

UpsellsCreateResult = TypedDict("UpsellsCreateResult", {
    "id": str,
    "kind": str,
    "name": str,
    "enabled": bool,
    "sells": str,
    "productId": Any,
    "variantId": Any,
    "productName": Any,
    "productImage": Any,
    "variantLabel": Any,
    "variantPrice": Any,
    "price": float,
    "cost": Any,
    "message": str,
    "offered": str,
    "charged": str,
    "trigger": str,
    "minSubtotal": Any,
    "discountType": str,
    "discountValue": float,
    "words": str,
    "startsAt": Any,
    "endsAt": Any,
    "firstOrders": bool,
    "hideOwned": bool,
    "targets": List[UpsellsCreateResultTargetsItem],
    "shown": float,
    "taken": float,
    "revenue": float,
    "dateCreated": str,
    "updatedAt": str,
})

UpsellsSortResult = TypedDict("UpsellsSortResult", {
    "sorted": float,
})

UpsellsSettingsResult = TypedDict("UpsellsSettingsResult", {
    "boughtTogetherAuto": bool,
})

UpsellsUpdateResultTargetsItem = TypedDict("UpsellsUpdateResultTargetsItem", {
    "type": str,
    "id": str,
    "name": str,
})

UpsellsUpdateResult = TypedDict("UpsellsUpdateResult", {
    "id": str,
    "kind": str,
    "name": str,
    "enabled": bool,
    "sells": str,
    "productId": Any,
    "variantId": Any,
    "productName": Any,
    "productImage": Any,
    "variantLabel": Any,
    "variantPrice": Any,
    "price": float,
    "cost": Any,
    "message": str,
    "offered": str,
    "charged": str,
    "trigger": str,
    "minSubtotal": Any,
    "discountType": str,
    "discountValue": float,
    "words": str,
    "startsAt": Any,
    "endsAt": Any,
    "firstOrders": bool,
    "hideOwned": bool,
    "targets": List[UpsellsUpdateResultTargetsItem],
    "shown": float,
    "taken": float,
    "revenue": float,
    "dateCreated": str,
    "updatedAt": str,
})

UpsellsDeleteResult = TypedDict("UpsellsDeleteResult", {
    "id": str,
    "deleted": bool,
})

UpsellsSetEnabledResultTargetsItem = TypedDict("UpsellsSetEnabledResultTargetsItem", {
    "type": str,
    "id": str,
    "name": str,
})

UpsellsSetEnabledResult = TypedDict("UpsellsSetEnabledResult", {
    "id": str,
    "kind": str,
    "name": str,
    "enabled": bool,
    "sells": str,
    "productId": Any,
    "variantId": Any,
    "productName": Any,
    "productImage": Any,
    "variantLabel": Any,
    "variantPrice": Any,
    "price": float,
    "cost": Any,
    "message": str,
    "offered": str,
    "charged": str,
    "trigger": str,
    "minSubtotal": Any,
    "discountType": str,
    "discountValue": float,
    "words": str,
    "startsAt": Any,
    "endsAt": Any,
    "firstOrders": bool,
    "hideOwned": bool,
    "targets": List[UpsellsSetEnabledResultTargetsItem],
    "shown": float,
    "taken": float,
    "revenue": float,
    "dateCreated": str,
    "updatedAt": str,
})

SubscriptionsListItem = TypedDict("SubscriptionsListItem", {
    "id": str,
    "email": str,
    "customerId": Any,
    "productId": str,
    "variantId": str,
    "productName": str,
    "variantName": str,
    "quantity": float,
    "price": float,
    "currency": str,
    "every": float,
    "unit": str,
    "status": str,
    "periodEnd": str,
    "graceEnd": Any,
    "renewalOrderId": Any,
    "renewalUrl": Any,
    "firstOrderId": str,
    "cycles": float,
    "remindedAt": Any,
    "endedAt": Any,
    "revoked": bool,
    "pausedAt": Any,
    "resumeAt": Any,
    "pausedBy": Any,
    "renewsWith": Any,
    "autoRenews": bool,
    "chargeTried": float,
    "chargeNextAt": Any,
    "createdAt": str,
})

SubscriptionsSettingsResult = TypedDict("SubscriptionsSettingsResult", {
    "cancelOn": bool,
    "cancelMode": str,
    "undoOn": bool,
    "pauseOn": bool,
    "pauseDays": float,
    "pausesAYear": float,
    "remindersOn": bool,
    "reminderDays": List[float],
    "graceDays": float,
    "revokeOn": bool,
    "autoOn": bool,
    "cardChangeOn": bool,
    "chargeTries": float,
})

SubscriptionsUpdateSettingsResult = TypedDict("SubscriptionsUpdateSettingsResult", {
    "cancelOn": bool,
    "cancelMode": str,
    "undoOn": bool,
    "pauseOn": bool,
    "pauseDays": float,
    "pausesAYear": float,
    "remindersOn": bool,
    "reminderDays": List[float],
    "graceDays": float,
    "revokeOn": bool,
    "autoOn": bool,
    "cardChangeOn": bool,
    "chargeTries": float,
})

SubscriptionsPlansResultItem = TypedDict("SubscriptionsPlansResultItem", {
    "variantId": str,
    "productId": str,
    "productName": str,
    "variantName": str,
    "price": float,
    "every": float,
    "unit": str,
    "running": float,
    "automatic": float,
})

SubscriptionsSavePlansResultItem = TypedDict("SubscriptionsSavePlansResultItem", {
    "variantId": str,
    "productId": str,
    "productName": str,
    "variantName": str,
    "price": float,
    "every": float,
    "unit": str,
    "running": float,
    "automatic": float,
})

SubscriptionsShowResult = TypedDict("SubscriptionsShowResult", {
    "id": str,
    "email": str,
    "customerId": Any,
    "productId": str,
    "variantId": str,
    "productName": str,
    "variantName": str,
    "quantity": float,
    "price": float,
    "currency": str,
    "every": float,
    "unit": str,
    "status": str,
    "periodEnd": str,
    "graceEnd": Any,
    "renewalOrderId": Any,
    "renewalUrl": Any,
    "firstOrderId": str,
    "cycles": float,
    "remindedAt": Any,
    "endedAt": Any,
    "revoked": bool,
    "pausedAt": Any,
    "resumeAt": Any,
    "pausedBy": Any,
    "renewsWith": Any,
    "autoRenews": bool,
    "chargeTried": float,
    "chargeNextAt": Any,
    "createdAt": str,
})

SubscriptionsCancelResult = TypedDict("SubscriptionsCancelResult", {
    "id": str,
    "email": str,
    "customerId": Any,
    "productId": str,
    "variantId": str,
    "productName": str,
    "variantName": str,
    "quantity": float,
    "price": float,
    "currency": str,
    "every": float,
    "unit": str,
    "status": str,
    "periodEnd": str,
    "graceEnd": Any,
    "renewalOrderId": Any,
    "renewalUrl": Any,
    "firstOrderId": str,
    "cycles": float,
    "remindedAt": Any,
    "endedAt": Any,
    "revoked": bool,
    "pausedAt": Any,
    "resumeAt": Any,
    "pausedBy": Any,
    "renewsWith": Any,
    "autoRenews": bool,
    "chargeTried": float,
    "chargeNextAt": Any,
    "createdAt": str,
})

SubscriptionsUndoResult = TypedDict("SubscriptionsUndoResult", {
    "id": str,
    "email": str,
    "customerId": Any,
    "productId": str,
    "variantId": str,
    "productName": str,
    "variantName": str,
    "quantity": float,
    "price": float,
    "currency": str,
    "every": float,
    "unit": str,
    "status": str,
    "periodEnd": str,
    "graceEnd": Any,
    "renewalOrderId": Any,
    "renewalUrl": Any,
    "firstOrderId": str,
    "cycles": float,
    "remindedAt": Any,
    "endedAt": Any,
    "revoked": bool,
    "pausedAt": Any,
    "resumeAt": Any,
    "pausedBy": Any,
    "renewsWith": Any,
    "autoRenews": bool,
    "chargeTried": float,
    "chargeNextAt": Any,
    "createdAt": str,
})

SubscriptionsPauseResult = TypedDict("SubscriptionsPauseResult", {
    "id": str,
    "email": str,
    "customerId": Any,
    "productId": str,
    "variantId": str,
    "productName": str,
    "variantName": str,
    "quantity": float,
    "price": float,
    "currency": str,
    "every": float,
    "unit": str,
    "status": str,
    "periodEnd": str,
    "graceEnd": Any,
    "renewalOrderId": Any,
    "renewalUrl": Any,
    "firstOrderId": str,
    "cycles": float,
    "remindedAt": Any,
    "endedAt": Any,
    "revoked": bool,
    "pausedAt": str,
    "resumeAt": str,
    "pausedBy": str,
    "renewsWith": Any,
    "autoRenews": bool,
    "chargeTried": float,
    "chargeNextAt": Any,
    "createdAt": str,
})

SubscriptionsResumeResult = TypedDict("SubscriptionsResumeResult", {
    "id": str,
    "email": str,
    "customerId": Any,
    "productId": str,
    "variantId": str,
    "productName": str,
    "variantName": str,
    "quantity": float,
    "price": float,
    "currency": str,
    "every": float,
    "unit": str,
    "status": str,
    "periodEnd": str,
    "graceEnd": Any,
    "renewalOrderId": Any,
    "renewalUrl": Any,
    "firstOrderId": str,
    "cycles": float,
    "remindedAt": Any,
    "endedAt": Any,
    "revoked": bool,
    "pausedAt": Any,
    "resumeAt": Any,
    "pausedBy": Any,
    "renewsWith": Any,
    "autoRenews": bool,
    "chargeTried": float,
    "chargeNextAt": Any,
    "createdAt": str,
})

SubscriptionsAddDaysResult = TypedDict("SubscriptionsAddDaysResult", {
    "id": str,
    "email": str,
    "customerId": Any,
    "productId": str,
    "variantId": str,
    "productName": str,
    "variantName": str,
    "quantity": float,
    "price": float,
    "currency": str,
    "every": float,
    "unit": str,
    "status": str,
    "periodEnd": str,
    "graceEnd": Any,
    "renewalOrderId": Any,
    "renewalUrl": Any,
    "firstOrderId": str,
    "cycles": float,
    "remindedAt": Any,
    "endedAt": Any,
    "revoked": bool,
    "pausedAt": Any,
    "resumeAt": Any,
    "pausedBy": Any,
    "renewsWith": Any,
    "autoRenews": bool,
    "chargeTried": float,
    "chargeNextAt": Any,
    "createdAt": str,
})

SubscriptionsEmailResult = TypedDict("SubscriptionsEmailResult", {
    "id": str,
    "email": str,
    "customerId": Any,
    "productId": str,
    "variantId": str,
    "productName": str,
    "variantName": str,
    "quantity": float,
    "price": float,
    "currency": str,
    "every": float,
    "unit": str,
    "status": str,
    "periodEnd": str,
    "graceEnd": Any,
    "renewalOrderId": str,
    "renewalUrl": str,
    "firstOrderId": str,
    "cycles": float,
    "remindedAt": str,
    "endedAt": Any,
    "revoked": bool,
    "pausedAt": Any,
    "resumeAt": Any,
    "pausedBy": Any,
    "renewsWith": Any,
    "autoRenews": bool,
    "chargeTried": float,
    "chargeNextAt": Any,
    "createdAt": str,
})

OrdersListItemBilling = TypedDict("OrdersListItemBilling", {
    "name": str,
    "line1": str,
    "line2": str,
    "city": str,
    "state": str,
    "postalCode": str,
    "country": str,
})

OrdersListItemItemsItem = TypedDict("OrdersListItemItemsItem", {
    "id": str,
    "productId": str,
    "productName": str,
    "variantId": str,
    "variantName": str,
    "amount": float,
    "unitPrice": float,
    "quantity": float,
    "lineTotal": float,
    "upsellId": Any,
    "addonOf": Any,
    "deliveredKeys": Union[List[Any], Dict[str, Any]],
    "redeliveryCount": float,
    "lastRedeliveredAt": Any,
    "deliveryInstructions": str,
    "dynamicState": str,
    "dynamicMessage": str,
    "dynamicItems": Union[List[Any], Dict[str, Any]],
    "previousDynamicItems": Union[List[Any], Dict[str, Any]],
    "dynamicDeliveredAt": Any,
    "dynamicError": str,
    "dynamicAttempts": float,
})

OrdersListItem = TypedDict("OrdersListItem", {
    "id": str,
    "dateCreated": str,
    "email": str,
    "customerId": str,
    "productId": str,
    "productName": str,
    "variantId": str,
    "variantName": str,
    "itemCount": float,
    "subtotal": float,
    "discount": float,
    "fee": float,
    "balanceUsed": float,
    "tax": Any,
    "amount": float,
    "currencyCode": str,
    "charged": Any,
    "status": str,
    "gateway": str,
    "couponCode": Any,
    "returning": bool,
    "country": Any,
    "billing": OrdersListItemBilling,
    "ip": Any,
    "userAgent": Any,
    "source": str,
    "subscriptionId": Any,
    "transactionId": Any,
    "paidAt": Any,
    "note": str,
    "customFields": Union[List[Any], Dict[str, Any]],
    "emailState": str,
    "emailError": str,
    "emailAttempts": float,
    "emailSentAt": Any,
    "notifyState": str,
    "notifyError": str,
    "notifyAttempts": float,
    "notifySentAt": Any,
    "summary": str,
    "items": List[OrdersListItemItemsItem],
    "invoice": Any,
})

OrdersShowResultBilling = TypedDict("OrdersShowResultBilling", {
    "name": str,
    "line1": str,
    "line2": str,
    "city": str,
    "state": str,
    "postalCode": str,
    "country": str,
})

OrdersShowResultItemsItem = TypedDict("OrdersShowResultItemsItem", {
    "id": str,
    "productId": str,
    "productName": str,
    "variantId": str,
    "variantName": str,
    "amount": float,
    "unitPrice": float,
    "quantity": float,
    "lineTotal": float,
    "upsellId": Any,
    "addonOf": Any,
    "deliveredKeys": List[str],
    "redeliveryCount": float,
    "lastRedeliveredAt": Any,
    "deliveryInstructions": str,
    "dynamicState": str,
    "dynamicMessage": str,
    "dynamicItems": Union[List[Any], Dict[str, Any]],
    "previousDynamicItems": Union[List[Any], Dict[str, Any]],
    "dynamicDeliveredAt": Any,
    "dynamicError": str,
    "dynamicAttempts": float,
    "redeliverable": bool,
    "stockAvailable": float,
    "previousKeys": Union[List[Any], Dict[str, Any]],
})

OrdersShowResultRefundSource = TypedDict("OrdersShowResultRefundSource", {
    "available": bool,
    "why": str,
    "provider": str,
    "name": str,
})

OrdersShowResultRefundBalance = TypedDict("OrdersShowResultRefundBalance", {
    "available": bool,
    "why": str,
})

OrdersShowResultRefundRecord = TypedDict("OrdersShowResultRefundRecord", {
    "available": bool,
    "why": str,
})

OrdersShowResultRefund = TypedDict("OrdersShowResultRefund", {
    "amount": float,
    "currency": str,
    "fromBalance": float,
    "paid": float,
    "source": OrdersShowResultRefundSource,
    "balance": OrdersShowResultRefundBalance,
    "record": OrdersShowResultRefundRecord,
})

OrdersShowResultCustomer = TypedDict("OrdersShowResultCustomer", {
    "id": str,
    "emailAddress": str,
    "dateCreated": str,
})

OrdersShowResultTimelineItem = TypedDict("OrdersShowResultTimelineItem", {
    "id": str,
    "kind": str,
    "detail": str,
    "actor": str,
    "at": str,
})

OrdersShowResultCustomerTotals = TypedDict("OrdersShowResultCustomerTotals", {
    "totalOrders": float,
    "totalSpend": float,
    "paidOrders": float,
})

OrdersShowResultCustomerOrdersItem = TypedDict("OrdersShowResultCustomerOrdersItem", {
    "id": str,
    "productName": str,
    "variantName": str,
    "itemCount": float,
    "amount": float,
    "status": str,
    "dateCreated": str,
})

OrdersShowResult = TypedDict("OrdersShowResult", {
    "id": str,
    "dateCreated": str,
    "email": str,
    "customerId": str,
    "productId": str,
    "productName": str,
    "variantId": str,
    "variantName": str,
    "itemCount": float,
    "subtotal": float,
    "discount": float,
    "fee": float,
    "balanceUsed": float,
    "tax": Any,
    "amount": float,
    "currencyCode": str,
    "charged": Any,
    "status": str,
    "gateway": str,
    "couponCode": Any,
    "returning": bool,
    "country": Any,
    "billing": OrdersShowResultBilling,
    "ip": Any,
    "userAgent": Any,
    "source": str,
    "subscriptionId": Any,
    "transactionId": str,
    "paidAt": str,
    "note": str,
    "customFields": Union[List[Any], Dict[str, Any]],
    "emailState": str,
    "emailError": str,
    "emailAttempts": float,
    "emailSentAt": str,
    "notifyState": str,
    "notifyError": str,
    "notifyAttempts": float,
    "notifySentAt": Any,
    "summary": str,
    "items": List[OrdersShowResultItemsItem],
    "refund": OrdersShowResultRefund,
    "productSlug": str,
    "imageUrl": Any,
    "customer": OrdersShowResultCustomer,
    "visit": Any,
    "affiliate": Any,
    "timeline": List[OrdersShowResultTimelineItem],
    "testPayment": bool,
    "payments": Union[List[Any], Dict[str, Any]],
    "invoice": Any,
    "disputes": Union[List[Any], Dict[str, Any]],
    "review": Any,
    "requests": Union[List[Any], Dict[str, Any]],
    "customPayment": Any,
    "customerTotals": OrdersShowResultCustomerTotals,
    "customerOrders": List[OrdersShowResultCustomerOrdersItem],
})

OrdersMarkPaidResult = TypedDict("OrdersMarkPaidResult", {
    "id": str,
    "status": str,
    "dynamic": Union[List[Any], Dict[str, Any]],
})

OrdersRefundResult = TypedDict("OrdersRefundResult", {
    "id": str,
    "status": str,
    "destination": str,
})

OrdersRedeliverResultItemsItem = TypedDict("OrdersRedeliverResultItemsItem", {
    "id": float,
    "productName": str,
    "variantName": str,
    "keys": List[str],
})

OrdersRedeliverResultEmail = TypedDict("OrdersRedeliverResultEmail", {
    "state": str,
    "reason": str,
})

OrdersRedeliverResult = TypedDict("OrdersRedeliverResult", {
    "id": str,
    "items": List[OrdersRedeliverResultItemsItem],
    "email": OrdersRedeliverResultEmail,
    "dynamic": Union[List[Any], Dict[str, Any]],
})

OrdersApprovePaymentResult = TypedDict("OrdersApprovePaymentResult", {
    "id": str,
    "status": str,
    "dynamic": Union[List[Any], Dict[str, Any]],
})

OrdersRejectPaymentResult = TypedDict("OrdersRejectPaymentResult", {
    "id": str,
    "status": str,
})

OrdersSetNoteResult = TypedDict("OrdersSetNoteResult", {
    "id": str,
})

InvoicesListItem = TypedDict("InvoicesListItem", {
    "orderId": str,
    "number": float,
    "label": str,
    "recipientName": str,
    "note": str,
    "gateways": List[str],
    "dueAt": str,
    "overdue": bool,
    "sentAt": Any,
    "sendCount": float,
    "dateCreated": str,
    "payUrl": str,
    "kind": str,
    "title": str,
    "uses": Any,
    "linkOf": str,
    "charge": Any,
    "email": str,
    "amount": float,
    "currencyCode": str,
    "status": str,
    "itemCount": float,
    "paidAt": Any,
})

InvoicesLinkResult = TypedDict("InvoicesLinkResult", {
    "orderId": str,
    "number": float,
    "label": str,
    "recipientName": str,
    "note": str,
    "gateways": List[str],
    "dueAt": str,
    "overdue": bool,
    "sentAt": Any,
    "sendCount": float,
    "dateCreated": str,
    "payUrl": str,
    "kind": str,
    "title": str,
    "uses": Any,
    "linkOf": str,
    "charge": Any,
    "email": str,
    "amount": float,
    "currencyCode": str,
    "status": str,
    "itemCount": float,
    "paidAt": Any,
})

ReviewsListItemItemsItem = TypedDict("ReviewsListItemItemsItem", {
    "productId": str,
    "productName": str,
    "variantName": str,
})

ReviewsListItemFlag = TypedDict("ReviewsListItemFlag", {
    "id": str,
    "status": str,
    "reason": str,
    "reasonLabel": str,
    "note": str,
    "answer": str,
    "dateCreated": str,
    "dateDecided": Any,
})

ReviewsListItem = TypedDict("ReviewsListItem", {
    "id": str,
    "rating": float,
    "message": str,
    "automatic": bool,
    "dateCreated": str,
    "items": List[ReviewsListItemItemsItem],
    "orderId": str,
    "customerId": str,
    "email": str,
    "orderAmount": float,
    "currencyCode": str,
    "flag": ReviewsListItemFlag,
})

CouponsListItem = TypedDict("CouponsListItem", {
    "id": str,
    "storeId": str,
    "categoryId": str,
    "code": str,
    "discountType": str,
    "value": float,
    "maxUses": float,
    "uses": float,
    "remainingUses": float,
    "minSubtotal": float,
    "expiresAt": Any,
    "active": bool,
    "appliesTo": str,
    "targets": Union[List[Any], Dict[str, Any]],
    "sort": float,
    "discountGiven": float,
    "revenue": float,
    "dateCreated": str,
    "updatedAt": str,
})

CouponsCreateResult = TypedDict("CouponsCreateResult", {
    "id": str,
    "storeId": str,
    "categoryId": str,
    "code": str,
    "discountType": str,
    "value": float,
    "maxUses": float,
    "uses": float,
    "remainingUses": float,
    "minSubtotal": float,
    "expiresAt": Any,
    "active": bool,
    "appliesTo": str,
    "targets": Union[List[Any], Dict[str, Any]],
    "sort": float,
    "discountGiven": float,
    "revenue": float,
    "dateCreated": str,
    "updatedAt": str,
})

CouponsUpdateResult = TypedDict("CouponsUpdateResult", {
    "id": str,
    "storeId": str,
    "categoryId": str,
    "code": str,
    "discountType": str,
    "value": float,
    "maxUses": float,
    "uses": float,
    "remainingUses": float,
    "minSubtotal": float,
    "expiresAt": Any,
    "active": bool,
    "appliesTo": str,
    "targets": Union[List[Any], Dict[str, Any]],
    "sort": float,
    "discountGiven": float,
    "revenue": float,
    "dateCreated": str,
    "updatedAt": str,
})

CouponsDeleteResult = TypedDict("CouponsDeleteResult", {
    "id": str,
    "deleted": bool,
})

CouponsSortResult = TypedDict("CouponsSortResult", {
    "reordered": float,
})

CouponCategoriesListResultItem = TypedDict("CouponCategoriesListResultItem", {
    "id": str,
    "storeId": str,
    "name": str,
    "slug": str,
    "description": str,
    "sort": float,
    "systemKey": str,
    "couponCount": float,
    "activeCount": float,
    "uses": float,
    "discountGiven": float,
    "dateCreated": str,
    "updatedAt": str,
})

CouponCategoriesCreateResult = TypedDict("CouponCategoriesCreateResult", {
    "id": str,
    "storeId": str,
    "name": str,
    "slug": str,
    "description": str,
    "sort": float,
    "systemKey": str,
    "couponCount": float,
    "activeCount": float,
    "uses": float,
    "discountGiven": float,
    "dateCreated": str,
    "updatedAt": str,
})

CouponCategoriesUpdateResult = TypedDict("CouponCategoriesUpdateResult", {
    "id": str,
    "storeId": str,
    "name": str,
    "slug": str,
    "description": str,
    "sort": float,
    "systemKey": str,
    "couponCount": float,
    "activeCount": float,
    "uses": float,
    "discountGiven": float,
    "dateCreated": str,
    "updatedAt": str,
})

CouponCategoriesDeleteResult = TypedDict("CouponCategoriesDeleteResult", {
    "id": str,
    "deleted": bool,
    "moved": float,
})

CouponPopupShowResult = TypedDict("CouponPopupShowResult", {
    "enabled": bool,
    "couponId": str,
    "coupon": Any,
    "title": str,
    "message": str,
    "buttonText": str,
    "opens": str,
    "delaySeconds": float,
    "frequency": str,
    "updatedAt": Any,
})

CouponPopupUpdateResultCoupon = TypedDict("CouponPopupUpdateResultCoupon", {
    "id": str,
    "code": str,
    "discountType": str,
    "value": float,
    "minSubtotal": float,
    "expiresAt": Any,
    "appliesTo": str,
    "unusable": str,
    "pausedBySale": bool,
})

CouponPopupUpdateResult = TypedDict("CouponPopupUpdateResult", {
    "enabled": bool,
    "couponId": str,
    "coupon": CouponPopupUpdateResultCoupon,
    "title": str,
    "message": str,
    "buttonText": str,
    "opens": str,
    "delaySeconds": float,
    "frequency": str,
    "updatedAt": str,
})

SalesListResultItem = TypedDict("SalesListResultItem", {
    "id": str,
    "name": str,
    "enabled": bool,
    "status": str,
    "discountType": str,
    "value": float,
    "appliesTo": str,
    "targets": Union[List[Any], Dict[str, Any]],
    "startsAt": str,
    "endsAt": str,
    "couponRule": str,
    "exceptions": Union[List[Any], Dict[str, Any]],
    "showBar": bool,
    "orders": float,
    "revenue": float,
    "dateCreated": str,
    "updatedAt": str,
})

SalesCreateResult = TypedDict("SalesCreateResult", {
    "id": str,
    "name": str,
    "enabled": bool,
    "status": str,
    "discountType": str,
    "value": float,
    "appliesTo": str,
    "targets": Union[List[Any], Dict[str, Any]],
    "startsAt": str,
    "endsAt": str,
    "couponRule": str,
    "exceptions": Union[List[Any], Dict[str, Any]],
    "showBar": bool,
    "orders": float,
    "revenue": float,
    "dateCreated": str,
    "updatedAt": str,
})

SalesShowResult = TypedDict("SalesShowResult", {
    "id": str,
    "name": str,
    "enabled": bool,
    "status": str,
    "discountType": str,
    "value": float,
    "appliesTo": str,
    "targets": Union[List[Any], Dict[str, Any]],
    "startsAt": str,
    "endsAt": str,
    "couponRule": str,
    "exceptions": Union[List[Any], Dict[str, Any]],
    "showBar": bool,
    "orders": float,
    "revenue": float,
    "dateCreated": str,
    "updatedAt": str,
})

SalesDeleteResult = TypedDict("SalesDeleteResult", {
    "id": str,
    "deleted": bool,
})

SalesSetEnabledResult = TypedDict("SalesSetEnabledResult", {
    "id": str,
    "name": str,
    "enabled": bool,
    "status": str,
    "discountType": str,
    "value": float,
    "appliesTo": str,
    "targets": Union[List[Any], Dict[str, Any]],
    "startsAt": str,
    "endsAt": str,
    "couponRule": str,
    "exceptions": Union[List[Any], Dict[str, Any]],
    "showBar": bool,
    "orders": float,
    "revenue": float,
    "dateCreated": str,
    "updatedAt": str,
})

BlogListResultItemPostsItem = TypedDict("BlogListResultItemPostsItem", {
    "id": str,
    "categoryId": str,
    "title": str,
    "slug": str,
    "path": str,
    "status": str,
    "coverUrl": Any,
    "views": float,
    "publishedAt": str,
    "updatedAt": str,
})

BlogListResultItem = TypedDict("BlogListResultItem", {
    "id": str,
    "name": str,
    "slug": str,
    "path": str,
    "description": str,
    "imageUrl": Any,
    "posts": List[BlogListResultItemPostsItem],
})

BlogCategoriesCreateResult = TypedDict("BlogCategoriesCreateResult", {
    "id": str,
    "name": str,
    "slug": str,
    "path": str,
    "description": str,
    "imageUrl": Any,
    "posts": Union[List[Any], Dict[str, Any]],
})

BlogCategoriesUpdateResult = TypedDict("BlogCategoriesUpdateResult", {
    "id": str,
    "name": str,
    "slug": str,
    "path": str,
    "description": str,
    "imageUrl": Any,
})

BlogCategoriesDeleteResult = TypedDict("BlogCategoriesDeleteResult", {
    "id": str,
    "deleted": bool,
})

BlogCategoriesSortResult = TypedDict("BlogCategoriesSortResult", {
    "reordered": float,
})

BlogPostsCreateResultSearchChecksItem = TypedDict("BlogPostsCreateResultSearchChecksItem", {
    "ok": bool,
    "text": str,
})

BlogPostsCreateResultSearch = TypedDict("BlogPostsCreateResultSearch", {
    "title": str,
    "description": str,
    "html": str,
    "checks": List[BlogPostsCreateResultSearchChecksItem],
})

BlogPostsCreateResult = TypedDict("BlogPostsCreateResult", {
    "id": str,
    "categoryId": str,
    "title": str,
    "slug": str,
    "path": str,
    "status": str,
    "coverUrl": Any,
    "views": float,
    "publishedAt": Any,
    "updatedAt": str,
    "body": str,
    "coverAlt": str,
    "seoTitle": str,
    "seoDescription": str,
    "url": str,
    "search": BlogPostsCreateResultSearch,
})

BlogPostsShowResultSearchChecksItem = TypedDict("BlogPostsShowResultSearchChecksItem", {
    "ok": bool,
    "text": str,
})

BlogPostsShowResultSearch = TypedDict("BlogPostsShowResultSearch", {
    "title": str,
    "description": str,
    "html": str,
    "checks": List[BlogPostsShowResultSearchChecksItem],
})

BlogPostsShowResult = TypedDict("BlogPostsShowResult", {
    "id": str,
    "categoryId": str,
    "title": str,
    "slug": str,
    "path": str,
    "status": str,
    "coverUrl": Any,
    "views": float,
    "publishedAt": str,
    "updatedAt": str,
    "body": str,
    "coverAlt": str,
    "seoTitle": str,
    "seoDescription": str,
    "url": str,
    "search": BlogPostsShowResultSearch,
})

BlogPostsUpdateResultSearchChecksItem = TypedDict("BlogPostsUpdateResultSearchChecksItem", {
    "ok": bool,
    "text": str,
})

BlogPostsUpdateResultSearch = TypedDict("BlogPostsUpdateResultSearch", {
    "title": str,
    "description": str,
    "html": str,
    "checks": List[BlogPostsUpdateResultSearchChecksItem],
})

BlogPostsUpdateResult = TypedDict("BlogPostsUpdateResult", {
    "id": str,
    "categoryId": str,
    "title": str,
    "slug": str,
    "path": str,
    "status": str,
    "coverUrl": Any,
    "views": float,
    "publishedAt": Any,
    "updatedAt": str,
    "body": str,
    "coverAlt": str,
    "seoTitle": str,
    "seoDescription": str,
    "url": str,
    "search": BlogPostsUpdateResultSearch,
})

BlogPostsDeleteResult = TypedDict("BlogPostsDeleteResult", {
    "id": str,
    "deleted": bool,
})

BlogPostsSetStatusResult = TypedDict("BlogPostsSetStatusResult", {
    "id": str,
    "categoryId": str,
    "title": str,
    "slug": str,
    "path": str,
    "status": str,
    "coverUrl": Any,
    "views": float,
    "publishedAt": str,
    "updatedAt": str,
})

BlogPostsSortResult = TypedDict("BlogPostsSortResult", {
    "reordered": float,
})

SeoShowResultAnalytics = TypedDict("SeoShowResultAnalytics", {
    "measurementId": str,
    "hasSecret": bool,
})

SeoShowResult = TypedDict("SeoShowResult", {
    "googleVerification": str,
    "bingVerification": str,
    "aiCrawlers": bool,
    "indexNow": bool,
    "analytics": SeoShowResultAnalytics,
})

SeoUpdateResultAnalytics = TypedDict("SeoUpdateResultAnalytics", {
    "measurementId": str,
    "hasSecret": bool,
})

SeoUpdateResult = TypedDict("SeoUpdateResult", {
    "googleVerification": str,
    "bingVerification": str,
    "aiCrawlers": bool,
    "indexNow": bool,
    "analytics": SeoUpdateResultAnalytics,
})

RedirectsListResultItem = TypedDict("RedirectsListResultItem", {
    "id": str,
    "from": str,
    "to": str,
    "hits": float,
    "createdAt": str,
    "live": bool,
})

RedirectsCreateResultItem = TypedDict("RedirectsCreateResultItem", {
    "id": str,
    "from": str,
    "to": str,
    "hits": float,
    "createdAt": str,
    "live": bool,
})

RedirectsUpdateResultItem = TypedDict("RedirectsUpdateResultItem", {
    "id": str,
    "from": str,
    "to": str,
    "hits": float,
    "createdAt": str,
    "live": bool,
})

SitemapShowResultKindsItemEntriesItem = TypedDict("SitemapShowResultKindsItemEntriesItem", {
    "ref": str,
    "name": str,
    "path": str,
    "changed": str,
    "on": bool,
    "priority": str,
    "changefreq": str,
})

SitemapShowResultKindsItem = TypedDict("SitemapShowResultKindsItem", {
    "id": str,
    "listed": bool,
    "priority": str,
    "changefreq": str,
    "entries": List[SitemapShowResultKindsItemEntriesItem],
})

SitemapShowResult = TypedDict("SitemapShowResult", {
    "url": str,
    "served": bool,
    "total": float,
    "listed": float,
    "priorities": List[str],
    "frequencies": List[str],
    "kinds": List[SitemapShowResultKindsItem],
})

SitemapUpdateKindResultKindsItemEntriesItem = TypedDict("SitemapUpdateKindResultKindsItemEntriesItem", {
    "ref": str,
    "name": str,
    "path": str,
    "changed": str,
    "on": bool,
    "priority": str,
    "changefreq": str,
})

SitemapUpdateKindResultKindsItem = TypedDict("SitemapUpdateKindResultKindsItem", {
    "id": str,
    "listed": bool,
    "priority": str,
    "changefreq": str,
    "entries": List[SitemapUpdateKindResultKindsItemEntriesItem],
})

SitemapUpdateKindResult = TypedDict("SitemapUpdateKindResult", {
    "url": str,
    "served": bool,
    "total": float,
    "listed": float,
    "priorities": List[str],
    "frequencies": List[str],
    "kinds": List[SitemapUpdateKindResultKindsItem],
})

CartRecoveryShowResult = TypedDict("CartRecoveryShowResult", {
    "enabled": bool,
    "firstOn": bool,
    "firstMinutes": float,
    "firstSubject": str,
    "declinedOn": bool,
    "declinedMinutes": float,
    "declinedSubject": str,
    "secondOn": bool,
    "secondMinutes": float,
    "secondSubject": str,
    "secondPercent": float,
})

CartRecoveryUpdateResult = TypedDict("CartRecoveryUpdateResult", {
    "enabled": bool,
    "firstOn": bool,
    "firstMinutes": float,
    "firstSubject": str,
    "declinedOn": bool,
    "declinedMinutes": float,
    "declinedSubject": str,
    "secondOn": bool,
    "secondMinutes": float,
    "secondSubject": str,
    "secondPercent": float,
})

CartRecoveryCartsItem = TypedDict("CartRecoveryCartsItem", {
    "id": str,
    "email": str,
    "total": float,
    "currency": str,
    "what": str,
    "leftAt": str,
    "state": str,
    "note": str,
    "clickedAt": Any,
    "emailedAt": Any,
    "secondEmailAt": Any,
    "couponCode": Any,
    "recoveredOrderId": Any,
    "recoveredAt": Any,
})

CartRecoveryCartResult = TypedDict("CartRecoveryCartResult", {
    "id": str,
    "email": str,
    "total": float,
    "currency": str,
    "what": str,
    "leftAt": str,
    "state": str,
    "note": str,
    "clickedAt": Any,
    "emailedAt": Any,
    "secondEmailAt": Any,
    "couponCode": Any,
    "recoveredOrderId": Any,
    "recoveredAt": Any,
})

CustomersListItem = TypedDict("CustomersListItem", {
    "id": str,
    "emailAddress": str,
    "dateCreated": str,
    "totalOrders": float,
    "totalSpend": float,
    "paidOrders": float,
    "lastOrderAt": Any,
    "balance": float,
    "affiliateState": Any,
})

CustomersCreateResult = TypedDict("CustomersCreateResult", {
    "id": str,
    "emailAddress": str,
    "dateCreated": str,
    "totalOrders": float,
    "totalSpend": float,
    "paidOrders": float,
    "lastOrderAt": Any,
    "balance": float,
    "affiliateState": Any,
})

CustomersStatsResultRange = TypedDict("CustomersStatsResultRange", {
    "preset": str,
    "from": str,
    "to": str,
})

CustomersStatsResultCustomers = TypedDict("CustomersStatsResultCustomers", {
    "total": float,
    "change": Any,
})

CustomersStatsResultNewCustomers = TypedDict("CustomersStatsResultNewCustomers", {
    "count": float,
    "previous": float,
    "change": Any,
})

CustomersStatsResultReturning = TypedDict("CustomersStatsResultReturning", {
    "rate": float,
    "returning": float,
    "customers": float,
    "change": Any,
})

CustomersStatsResultAverageSpend = TypedDict("CustomersStatsResultAverageSpend", {
    "value": float,
    "previous": float,
    "change": Any,
})

CustomersStatsResult = TypedDict("CustomersStatsResult", {
    "range": CustomersStatsResultRange,
    "currencyCode": str,
    "customers": CustomersStatsResultCustomers,
    "newCustomers": CustomersStatsResultNewCustomers,
    "returning": CustomersStatsResultReturning,
    "averageSpend": CustomersStatsResultAverageSpend,
})

CustomersShowResultBalanceHistoryItem = TypedDict("CustomersShowResultBalanceHistoryItem", {
    "id": str,
    "kind": str,
    "amount": float,
    "balanceAfter": float,
    "currencyCode": str,
    "note": str,
    "orderId": Any,
    "by": str,
    "dateCreated": str,
})

CustomersShowResult = TypedDict("CustomersShowResult", {
    "balance": float,
    "balanceAtCheckout": bool,
    "balanceHistory": List[CustomersShowResultBalanceHistoryItem],
    "affiliate": Any,
    "blacklisted": bool,
    "blacklistedBy": Union[List[Any], Dict[str, Any]],
    "blacklistRules": float,
    "knownAddresses": float,
    "id": str,
    "emailAddress": str,
    "dateCreated": str,
    "totalOrders": float,
    "totalSpend": float,
    "paidOrders": float,
    "lastOrderAt": Any,
    "currencyCode": str,
    "ordersTruncated": bool,
    "orders": Union[List[Any], Dict[str, Any]],
})

CustomersSetBalanceResultBalanceHistoryItem = TypedDict("CustomersSetBalanceResultBalanceHistoryItem", {
    "id": str,
    "kind": str,
    "amount": float,
    "balanceAfter": float,
    "currencyCode": str,
    "note": str,
    "orderId": Any,
    "by": str,
    "dateCreated": str,
})

CustomersSetBalanceResult = TypedDict("CustomersSetBalanceResult", {
    "balance": float,
    "balanceAtCheckout": bool,
    "balanceHistory": List[CustomersSetBalanceResultBalanceHistoryItem],
    "affiliate": Any,
    "blacklisted": bool,
    "blacklistedBy": Union[List[Any], Dict[str, Any]],
    "blacklistRules": float,
    "knownAddresses": float,
})

CustomersBlacklistResultBalanceHistoryItem = TypedDict("CustomersBlacklistResultBalanceHistoryItem", {
    "id": str,
    "kind": str,
    "amount": float,
    "balanceAfter": float,
    "currencyCode": str,
    "note": str,
    "orderId": Any,
    "by": str,
    "dateCreated": str,
})

CustomersBlacklistResultBlacklistedByItem = TypedDict("CustomersBlacklistResultBlacklistedByItem", {
    "id": str,
    "type": str,
    "value": str,
    "part": str,
})

CustomersBlacklistResult = TypedDict("CustomersBlacklistResult", {
    "balance": float,
    "balanceAtCheckout": bool,
    "balanceHistory": List[CustomersBlacklistResultBalanceHistoryItem],
    "affiliate": Any,
    "blacklisted": bool,
    "blacklistedBy": List[CustomersBlacklistResultBlacklistedByItem],
    "blacklistRules": float,
    "knownAddresses": float,
    "added": float,
})

CustomersUnblacklistResultBalanceHistoryItem = TypedDict("CustomersUnblacklistResultBalanceHistoryItem", {
    "id": str,
    "kind": str,
    "amount": float,
    "balanceAfter": float,
    "currencyCode": str,
    "note": str,
    "orderId": Any,
    "by": str,
    "dateCreated": str,
})

CustomersUnblacklistResult = TypedDict("CustomersUnblacklistResult", {
    "balance": float,
    "balanceAtCheckout": bool,
    "balanceHistory": List[CustomersUnblacklistResultBalanceHistoryItem],
    "affiliate": Any,
    "blacklisted": bool,
    "blacklistedBy": Union[List[Any], Dict[str, Any]],
    "blacklistRules": float,
    "knownAddresses": float,
    "removed": float,
})

AffiliatesListResultItem = TypedDict("AffiliatesListResultItem", {
    "id": str,
    "customerId": str,
    "email": str,
    "code": str,
    "link": str,
    "commission": float,
    "discount": float,
    "active": bool,
    "clicks": float,
    "orders": float,
    "revenue": float,
    "earned": float,
    "balance": float,
    "requested": float,
    "paidOut": float,
    "paidAsCredit": float,
    "joinedThemselves": bool,
    "dateCreated": str,
})

AffiliatesCreateResult = TypedDict("AffiliatesCreateResult", {
    "id": str,
    "customerId": str,
    "email": str,
    "code": str,
    "link": str,
    "commission": float,
    "discount": float,
    "active": bool,
    "clicks": float,
    "orders": float,
    "revenue": float,
    "earned": float,
    "balance": float,
    "requested": float,
    "paidOut": float,
    "paidAsCredit": float,
    "joinedThemselves": bool,
    "dateCreated": str,
})

AffiliatesUpdateResult = TypedDict("AffiliatesUpdateResult", {
    "id": str,
    "customerId": str,
    "email": str,
    "code": str,
    "link": str,
    "commission": float,
    "discount": float,
    "active": bool,
    "clicks": float,
    "orders": float,
    "revenue": float,
    "earned": float,
    "balance": float,
    "requested": float,
    "paidOut": float,
    "paidAsCredit": float,
    "joinedThemselves": bool,
    "dateCreated": str,
})

AffiliatesDeleteResultItem = TypedDict("AffiliatesDeleteResultItem", {
    "id": str,
    "customerId": str,
    "email": str,
    "code": str,
    "link": str,
    "commission": float,
    "discount": float,
    "active": bool,
    "clicks": float,
    "orders": float,
    "revenue": float,
    "earned": float,
    "balance": float,
    "requested": float,
    "paidOut": float,
    "paidAsCredit": float,
    "joinedThemselves": bool,
    "dateCreated": str,
})

AffiliatesSetBalanceResult = TypedDict("AffiliatesSetBalanceResult", {
    "id": str,
    "customerId": str,
    "email": str,
    "code": str,
    "link": str,
    "commission": float,
    "discount": float,
    "active": bool,
    "clicks": float,
    "orders": float,
    "revenue": float,
    "earned": float,
    "balance": float,
    "requested": float,
    "paidOut": float,
    "paidAsCredit": float,
    "joinedThemselves": bool,
    "dateCreated": str,
})

AffiliatesHistoryResultChangesItem = TypedDict("AffiliatesHistoryResultChangesItem", {
    "id": str,
    "kind": str,
    "amount": float,
    "balanceAfter": float,
    "currencyCode": str,
    "dateCreated": str,
    "note": str,
    "orderId": Any,
    "by": str,
})

AffiliatesHistoryResult = TypedDict("AffiliatesHistoryResult", {
    "changes": List[AffiliatesHistoryResultChangesItem],
    "payouts": Union[List[Any], Dict[str, Any]],
})

AffiliateProgrammeShowResult = TypedDict("AffiliateProgrammeShowResult", {
    "enabled": bool,
    "defaultCommission": float,
    "defaultDiscount": float,
    "selfSignup": bool,
    "ownLinks": bool,
    "toStore": bool,
    "payouts": bool,
})

AffiliateProgrammeUpdateResult = TypedDict("AffiliateProgrammeUpdateResult", {
    "enabled": bool,
    "defaultCommission": float,
    "defaultDiscount": float,
    "selfSignup": bool,
    "ownLinks": bool,
    "toStore": bool,
    "payouts": bool,
})

BlacklistListItem = TypedDict("BlacklistListItem", {
    "id": str,
    "type": str,
    "value": str,
    "label": str,
    "note": str,
    "enabled": bool,
    "source": str,
    "customerId": Any,
    "orderId": Any,
    "hits": float,
    "lastHitAt": Any,
    "dateCreated": str,
    "updatedAt": str,
})

BlacklistCreateResult = TypedDict("BlacklistCreateResult", {
    "id": str,
    "type": str,
    "value": str,
    "label": str,
    "note": str,
    "enabled": bool,
    "source": str,
    "customerId": Any,
    "orderId": Any,
    "hits": float,
    "lastHitAt": Any,
    "dateCreated": str,
    "updatedAt": str,
})

BlacklistUpdateResult = TypedDict("BlacklistUpdateResult", {
    "id": str,
    "type": str,
    "value": str,
    "label": str,
    "note": str,
    "enabled": bool,
    "source": str,
    "customerId": Any,
    "orderId": Any,
    "hits": float,
    "lastHitAt": Any,
    "dateCreated": str,
    "updatedAt": str,
})

BlacklistDeleteResult = TypedDict("BlacklistDeleteResult", {
    "id": str,
})

BlacklistSetEnabledResult = TypedDict("BlacklistSetEnabledResult", {
    "id": str,
    "type": str,
    "value": str,
    "label": str,
    "note": str,
    "enabled": bool,
    "source": str,
    "customerId": Any,
    "orderId": Any,
    "hits": float,
    "lastHitAt": Any,
    "dateCreated": str,
    "updatedAt": str,
})

FraudEventsListItemBy = TypedDict("FraudEventsListItemBy", {
    "name": str,
    "email": str,
})

FraudEventsListItem = TypedDict("FraudEventsListItem", {
    "id": str,
    "reason": str,
    "orderId": Any,
    "email": str,
    "ip": str,
    "country": str,
    "ruleId": Any,
    "ruleType": str,
    "ruleValue": str,
    "detail": str,
    "attempts": float,
    "by": FraudEventsListItemBy,
    "dateCreated": str,
    "lastAt": str,
    "network": Any,
})

FraudSettingsShowResult = TypedDict("FraudSettingsShowResult", {
    "blockVpn": bool,
    "blockOnDispute": bool,
    "blockedCountries": Union[List[Any], Dict[str, Any]],
})

FraudSettingsUpdateResult = TypedDict("FraudSettingsUpdateResult", {
    "blockVpn": bool,
    "blockOnDispute": bool,
    "blockedCountries": List[str],
})

DisputesListItemAnswer = TypedDict("DisputesListItemAnswer", {
    "state": str,
    "at": Any,
    "by": str,
    "note": str,
})

DisputesListItem = TypedDict("DisputesListItem", {
    "id": str,
    "orderId": str,
    "email": str,
    "provider": str,
    "providerName": str,
    "externalId": str,
    "reason": str,
    "reasonText": str,
    "stage": str,
    "providerStatus": str,
    "status": str,
    "amount": float,
    "currency": str,
    "dueAt": str,
    "answer": DisputesListItemAnswer,
    "answeredFrom": str,
    "answerPlace": str,
    "accessTaken": bool,
    "dateCreated": str,
    "dateClosed": Any,
})

DisputesForOrderResultItemAnswer = TypedDict("DisputesForOrderResultItemAnswer", {
    "state": str,
    "at": Any,
    "by": str,
    "note": str,
})

DisputesForOrderResultItem = TypedDict("DisputesForOrderResultItem", {
    "id": str,
    "orderId": str,
    "email": str,
    "provider": str,
    "providerName": str,
    "externalId": str,
    "reason": str,
    "reasonText": str,
    "stage": str,
    "providerStatus": str,
    "status": str,
    "amount": float,
    "currency": str,
    "dueAt": str,
    "answer": DisputesForOrderResultItemAnswer,
    "answeredFrom": str,
    "answerPlace": str,
    "accessTaken": bool,
    "dateCreated": str,
    "dateClosed": Any,
})

DisputesGetResultAnswer = TypedDict("DisputesGetResultAnswer", {
    "state": str,
    "at": Any,
    "by": str,
    "note": str,
})

DisputesGetResultOrder = TypedDict("DisputesGetResultOrder", {
    "id": str,
    "status": str,
    "amount": float,
    "currency": str,
    "dateCreated": str,
})

DisputesGetResultCan = TypedDict("DisputesGetResultCan", {
    "edit": bool,
    "submit": bool,
    "accept": bool,
    "markSubmitted": bool,
})

DisputesGetResultRecordsItemFactsItem = TypedDict("DisputesGetResultRecordsItemFactsItem", {
    "key": str,
    "name": str,
    "value": str,
    "strong": bool,
})

DisputesGetResultRecordsItem = TypedDict("DisputesGetResultRecordsItem", {
    "key": str,
    "title": str,
    "facts": List[DisputesGetResultRecordsItemFactsItem],
})

DisputesGetResultDraft = TypedDict("DisputesGetResultDraft", {
    "decision": str,
    "contacted": str,
    "used": str,
    "words": str,
    "saved": bool,
    "statement": str,
})

DisputesGetResultAfterItem = TypedDict("DisputesGetResultAfterItem", {
    "key": str,
    "done": bool,
    "text": str,
})

DisputesGetResultHistoryItem = TypedDict("DisputesGetResultHistoryItem", {
    "at": str,
    "what": str,
    "detail": str,
})

DisputesGetResult = TypedDict("DisputesGetResult", {
    "id": str,
    "orderId": str,
    "email": str,
    "provider": str,
    "providerName": str,
    "externalId": str,
    "reason": str,
    "reasonText": str,
    "stage": str,
    "providerStatus": str,
    "status": str,
    "amount": float,
    "currency": str,
    "dueAt": str,
    "answer": DisputesGetResultAnswer,
    "answeredFrom": str,
    "answerPlace": str,
    "accessTaken": bool,
    "dateCreated": str,
    "dateClosed": Any,
    "order": DisputesGetResultOrder,
    "can": DisputesGetResultCan,
    "records": List[DisputesGetResultRecordsItem],
    "activity": List[str],
    "draft": DisputesGetResultDraft,
    "files": Union[List[Any], Dict[str, Any]],
    "after": List[DisputesGetResultAfterItem],
    "history": List[DisputesGetResultHistoryItem],
})

DisputesSaveDraftResultAnswer = TypedDict("DisputesSaveDraftResultAnswer", {
    "state": str,
    "at": Any,
    "by": str,
    "note": str,
})

DisputesSaveDraftResultOrder = TypedDict("DisputesSaveDraftResultOrder", {
    "id": str,
    "status": str,
    "amount": float,
    "currency": str,
    "dateCreated": str,
})

DisputesSaveDraftResultCan = TypedDict("DisputesSaveDraftResultCan", {
    "edit": bool,
    "submit": bool,
    "accept": bool,
    "markSubmitted": bool,
})

DisputesSaveDraftResultRecordsItemFactsItem = TypedDict("DisputesSaveDraftResultRecordsItemFactsItem", {
    "key": str,
    "name": str,
    "value": str,
    "strong": bool,
})

DisputesSaveDraftResultRecordsItem = TypedDict("DisputesSaveDraftResultRecordsItem", {
    "key": str,
    "title": str,
    "facts": List[DisputesSaveDraftResultRecordsItemFactsItem],
})

DisputesSaveDraftResultDraft = TypedDict("DisputesSaveDraftResultDraft", {
    "decision": str,
    "contacted": str,
    "used": str,
    "words": str,
    "saved": bool,
    "statement": str,
})

DisputesSaveDraftResultAfterItem = TypedDict("DisputesSaveDraftResultAfterItem", {
    "key": str,
    "done": bool,
    "text": str,
})

DisputesSaveDraftResultHistoryItem = TypedDict("DisputesSaveDraftResultHistoryItem", {
    "at": str,
    "what": str,
    "detail": str,
})

DisputesSaveDraftResult = TypedDict("DisputesSaveDraftResult", {
    "id": str,
    "orderId": str,
    "email": str,
    "provider": str,
    "providerName": str,
    "externalId": str,
    "reason": str,
    "reasonText": str,
    "stage": str,
    "providerStatus": str,
    "status": str,
    "amount": float,
    "currency": str,
    "dueAt": str,
    "answer": DisputesSaveDraftResultAnswer,
    "answeredFrom": str,
    "answerPlace": str,
    "accessTaken": bool,
    "dateCreated": str,
    "dateClosed": Any,
    "order": DisputesSaveDraftResultOrder,
    "can": DisputesSaveDraftResultCan,
    "records": List[DisputesSaveDraftResultRecordsItem],
    "activity": List[str],
    "draft": DisputesSaveDraftResultDraft,
    "files": Union[List[Any], Dict[str, Any]],
    "after": List[DisputesSaveDraftResultAfterItem],
    "history": List[DisputesSaveDraftResultHistoryItem],
})

DisputesMarkSubmittedResultAnswer = TypedDict("DisputesMarkSubmittedResultAnswer", {
    "state": str,
    "at": str,
    "by": str,
    "note": str,
})

DisputesMarkSubmittedResultOrder = TypedDict("DisputesMarkSubmittedResultOrder", {
    "id": str,
    "status": str,
    "amount": float,
    "currency": str,
    "dateCreated": str,
})

DisputesMarkSubmittedResultCan = TypedDict("DisputesMarkSubmittedResultCan", {
    "edit": bool,
    "submit": bool,
    "accept": bool,
    "markSubmitted": bool,
})

DisputesMarkSubmittedResultRecordsItemFactsItem = TypedDict("DisputesMarkSubmittedResultRecordsItemFactsItem", {
    "key": str,
    "name": str,
    "value": str,
    "strong": bool,
})

DisputesMarkSubmittedResultRecordsItem = TypedDict("DisputesMarkSubmittedResultRecordsItem", {
    "key": str,
    "title": str,
    "facts": List[DisputesMarkSubmittedResultRecordsItemFactsItem],
})

DisputesMarkSubmittedResultDraft = TypedDict("DisputesMarkSubmittedResultDraft", {
    "decision": str,
    "contacted": str,
    "used": str,
    "words": str,
    "saved": bool,
    "statement": str,
})

DisputesMarkSubmittedResultAfterItem = TypedDict("DisputesMarkSubmittedResultAfterItem", {
    "key": str,
    "done": bool,
    "text": str,
})

DisputesMarkSubmittedResultHistoryItem = TypedDict("DisputesMarkSubmittedResultHistoryItem", {
    "at": str,
    "what": str,
    "detail": str,
})

DisputesMarkSubmittedResult = TypedDict("DisputesMarkSubmittedResult", {
    "id": str,
    "orderId": str,
    "email": str,
    "provider": str,
    "providerName": str,
    "externalId": str,
    "reason": str,
    "reasonText": str,
    "stage": str,
    "providerStatus": str,
    "status": str,
    "amount": float,
    "currency": str,
    "dueAt": str,
    "answer": DisputesMarkSubmittedResultAnswer,
    "answeredFrom": str,
    "answerPlace": str,
    "accessTaken": bool,
    "dateCreated": str,
    "dateClosed": Any,
    "order": DisputesMarkSubmittedResultOrder,
    "can": DisputesMarkSubmittedResultCan,
    "records": List[DisputesMarkSubmittedResultRecordsItem],
    "activity": Union[List[Any], Dict[str, Any]],
    "draft": DisputesMarkSubmittedResultDraft,
    "files": Union[List[Any], Dict[str, Any]],
    "after": List[DisputesMarkSubmittedResultAfterItem],
    "history": List[DisputesMarkSubmittedResultHistoryItem],
})

DisputesAccessResultAnswer = TypedDict("DisputesAccessResultAnswer", {
    "state": str,
    "at": Any,
    "by": str,
    "note": str,
})

DisputesAccessResultOrder = TypedDict("DisputesAccessResultOrder", {
    "id": str,
    "status": str,
    "amount": float,
    "currency": str,
    "dateCreated": str,
})

DisputesAccessResultCan = TypedDict("DisputesAccessResultCan", {
    "edit": bool,
    "submit": bool,
    "accept": bool,
    "markSubmitted": bool,
})

DisputesAccessResultRecordsItemFactsItem = TypedDict("DisputesAccessResultRecordsItemFactsItem", {
    "key": str,
    "name": str,
    "value": str,
    "strong": bool,
})

DisputesAccessResultRecordsItem = TypedDict("DisputesAccessResultRecordsItem", {
    "key": str,
    "title": str,
    "facts": List[DisputesAccessResultRecordsItemFactsItem],
})

DisputesAccessResultDraft = TypedDict("DisputesAccessResultDraft", {
    "decision": str,
    "contacted": str,
    "used": str,
    "words": str,
    "saved": bool,
    "statement": str,
})

DisputesAccessResultAfterItem = TypedDict("DisputesAccessResultAfterItem", {
    "key": str,
    "done": bool,
    "text": str,
})

DisputesAccessResultHistoryItem = TypedDict("DisputesAccessResultHistoryItem", {
    "at": str,
    "what": str,
    "detail": str,
})

DisputesAccessResult = TypedDict("DisputesAccessResult", {
    "id": str,
    "orderId": str,
    "email": str,
    "provider": str,
    "providerName": str,
    "externalId": str,
    "reason": str,
    "reasonText": str,
    "stage": str,
    "providerStatus": str,
    "status": str,
    "amount": float,
    "currency": str,
    "dueAt": str,
    "answer": DisputesAccessResultAnswer,
    "answeredFrom": str,
    "answerPlace": str,
    "accessTaken": bool,
    "dateCreated": str,
    "dateClosed": Any,
    "order": DisputesAccessResultOrder,
    "can": DisputesAccessResultCan,
    "records": List[DisputesAccessResultRecordsItem],
    "activity": List[str],
    "draft": DisputesAccessResultDraft,
    "files": Union[List[Any], Dict[str, Any]],
    "after": List[DisputesAccessResultAfterItem],
    "history": List[DisputesAccessResultHistoryItem],
})

DisputesBlacklistResultAnswer = TypedDict("DisputesBlacklistResultAnswer", {
    "state": str,
    "at": Any,
    "by": str,
    "note": str,
})

DisputesBlacklistResultOrder = TypedDict("DisputesBlacklistResultOrder", {
    "id": str,
    "status": str,
    "amount": float,
    "currency": str,
    "dateCreated": str,
})

DisputesBlacklistResultCan = TypedDict("DisputesBlacklistResultCan", {
    "edit": bool,
    "submit": bool,
    "accept": bool,
    "markSubmitted": bool,
})

DisputesBlacklistResultRecordsItemFactsItem = TypedDict("DisputesBlacklistResultRecordsItemFactsItem", {
    "key": str,
    "name": str,
    "value": str,
    "strong": bool,
})

DisputesBlacklistResultRecordsItem = TypedDict("DisputesBlacklistResultRecordsItem", {
    "key": str,
    "title": str,
    "facts": List[DisputesBlacklistResultRecordsItemFactsItem],
})

DisputesBlacklistResultDraft = TypedDict("DisputesBlacklistResultDraft", {
    "decision": str,
    "contacted": str,
    "used": str,
    "words": str,
    "saved": bool,
    "statement": str,
})

DisputesBlacklistResultAfterItem = TypedDict("DisputesBlacklistResultAfterItem", {
    "key": str,
    "done": bool,
    "text": str,
})

DisputesBlacklistResultHistoryItem = TypedDict("DisputesBlacklistResultHistoryItem", {
    "at": str,
    "what": str,
    "detail": str,
})

DisputesBlacklistResult = TypedDict("DisputesBlacklistResult", {
    "id": str,
    "orderId": str,
    "email": str,
    "provider": str,
    "providerName": str,
    "externalId": str,
    "reason": str,
    "reasonText": str,
    "stage": str,
    "providerStatus": str,
    "status": str,
    "amount": float,
    "currency": str,
    "dueAt": str,
    "answer": DisputesBlacklistResultAnswer,
    "answeredFrom": str,
    "answerPlace": str,
    "accessTaken": bool,
    "dateCreated": str,
    "dateClosed": Any,
    "order": DisputesBlacklistResultOrder,
    "can": DisputesBlacklistResultCan,
    "records": List[DisputesBlacklistResultRecordsItem],
    "activity": List[str],
    "draft": DisputesBlacklistResultDraft,
    "files": Union[List[Any], Dict[str, Any]],
    "after": List[DisputesBlacklistResultAfterItem],
    "history": List[DisputesBlacklistResultHistoryItem],
})

DisputesSettingsResult = TypedDict("DisputesSettingsResult", {
    "blacklist": bool,
    "takeBackAccess": bool,
    "acceptSmall": bool,
    "acceptUnder": float,
    "autoSubmit": bool,
    "askAboveOn": bool,
    "askAbove": float,
    "emailOpened": bool,
    "emailClosed": bool,
    "discord": bool,
    "currency": str,
})

DisputesUpdateSettingsResult = TypedDict("DisputesUpdateSettingsResult", {
    "blacklist": bool,
    "takeBackAccess": bool,
    "acceptSmall": bool,
    "acceptUnder": float,
    "autoSubmit": bool,
    "askAboveOn": bool,
    "askAbove": float,
    "emailOpened": bool,
    "emailClosed": bool,
    "discord": bool,
    "currency": str,
})

FinanceAccessResult = TypedDict("FinanceAccessResult", {
    "open": bool,
    "missing": Union[List[Any], Dict[str, Any]],
})

FinanceProfitResultPeriod = TypedDict("FinanceProfitResultPeriod", {
    "from": str,
    "to": str,
    "label": str,
    "previousFrom": str,
    "previousTo": str,
    "previousLabel": str,
})

FinanceProfitResultNow = TypedDict("FinanceProfitResultNow", {
    "netSales": float,
    "orders": float,
    "costOfGoods": float,
    "fees": float,
    "commission": float,
    "expenses": float,
    "profit": float,
    "margin": float,
    "units": float,
    "uncosted": float,
})

FinanceProfitResultPrevious = TypedDict("FinanceProfitResultPrevious", {
    "netSales": float,
    "orders": float,
    "costOfGoods": float,
    "fees": float,
    "commission": float,
    "expenses": float,
    "profit": float,
    "margin": Any,
    "units": float,
    "uncosted": float,
})

FinanceProfitResultBreakEven = TypedDict("FinanceProfitResultBreakEven", {
    "orders": float,
    "reachedOn": Any,
    "each": float,
})

FinanceProfitResultFees = TypedDict("FinanceProfitResultFees", {
    "rated": bool,
    "unrated": List[str],
})

FinanceProfitResultMonthsItem = TypedDict("FinanceProfitResultMonthsItem", {
    "month": str,
    "sales": float,
    "profit": float,
})

FinanceProfitResultProductsItemVariantsItem = TypedDict("FinanceProfitResultProductsItemVariantsItem", {
    "id": str,
    "label": str,
    "price": float,
    "costAmount": float,
    "costPercent": Any,
    "sold": float,
    "sales": float,
    "cost": float,
    "uncosted": float,
    "profit": Any,
})

FinanceProfitResultProductsItem = TypedDict("FinanceProfitResultProductsItem", {
    "id": str,
    "name": str,
    "image": Any,
    "expenses": float,
    "variants": List[FinanceProfitResultProductsItemVariantsItem],
    "sold": float,
    "sales": float,
    "cost": float,
    "uncosted": float,
    "profit": Any,
    "costSet": str,
})

FinanceProfitResult = TypedDict("FinanceProfitResult", {
    "period": FinanceProfitResultPeriod,
    "currency": str,
    "now": FinanceProfitResultNow,
    "previous": FinanceProfitResultPrevious,
    "perOrder": float,
    "average": float,
    "breakEven": FinanceProfitResultBreakEven,
    "fees": FinanceProfitResultFees,
    "months": List[FinanceProfitResultMonthsItem],
    "products": List[FinanceProfitResultProductsItem],
})

FinanceAccountingResultPeriod = TypedDict("FinanceAccountingResultPeriod", {
    "from": str,
    "to": str,
    "label": str,
    "previousFrom": str,
    "previousTo": str,
    "previousLabel": str,
})

FinanceAccountingResultLinesItem = TypedDict("FinanceAccountingResultLinesItem", {
    "kind": str,
    "label": str,
})

FinanceAccountingResultTax = TypedDict("FinanceAccountingResultTax", {
    "now": float,
    "previous": float,
})

FinanceAccountingResultNow = TypedDict("FinanceAccountingResultNow", {
    "netSales": float,
    "grossProfit": float,
    "expenses": float,
    "profit": float,
    "margin": float,
})

FinanceAccountingResultPrevious = TypedDict("FinanceAccountingResultPrevious", {
    "netSales": float,
    "grossProfit": float,
    "expenses": float,
    "profit": float,
    "margin": Any,
})

FinanceAccountingResultChecksItem = TypedDict("FinanceAccountingResultChecksItem", {
    "text": str,
    "href": str,
    "action": str,
})

FinanceAccountingResultCounts = TypedDict("FinanceAccountingResultCounts", {
    "orders": float,
    "expenses": float,
})

FinanceAccountingResultCountriesItem = TypedDict("FinanceAccountingResultCountriesItem", {
    "country": str,
    "name": str,
    "orders": float,
    "amount": float,
    "share": float,
})

FinanceAccountingResultMethodsItem = TypedDict("FinanceAccountingResultMethodsItem", {
    "provider": str,
    "name": str,
    "orders": float,
    "volume": float,
    "fees": float,
    "rated": bool,
    "net": float,
})

FinanceAccountingResultTaxReport = TypedDict("FinanceAccountingResultTaxReport", {
    "rows": Union[List[Any], Dict[str, Any]],
    "taxable": float,
    "tax": float,
})

FinanceAccountingResult = TypedDict("FinanceAccountingResult", {
    "period": FinanceAccountingResultPeriod,
    "currency": str,
    "business": List[str],
    "lines": List[FinanceAccountingResultLinesItem],
    "tax": FinanceAccountingResultTax,
    "now": FinanceAccountingResultNow,
    "previous": FinanceAccountingResultPrevious,
    "checks": List[FinanceAccountingResultChecksItem],
    "counts": FinanceAccountingResultCounts,
    "countries": List[FinanceAccountingResultCountriesItem],
    "methods": List[FinanceAccountingResultMethodsItem],
    "taxReport": FinanceAccountingResultTaxReport,
})

FinanceSetCostResult = TypedDict("FinanceSetCostResult", {
    "variantId": str,
    "costAmount": float,
    "costPercent": Any,
    "stamped": float,
    "past": float,
})

FinancePaymentCostsResultRatesItem = TypedDict("FinancePaymentCostsResultRatesItem", {
    "provider": str,
    "name": str,
    "percent": float,
    "fixed": float,
})

FinancePaymentCostsResultLimits = TypedDict("FinancePaymentCostsResultLimits", {
    "percent": float,
    "fixed": float,
})

FinancePaymentCostsResult = TypedDict("FinancePaymentCostsResult", {
    "currency": str,
    "rates": List[FinancePaymentCostsResultRatesItem],
    "limits": FinancePaymentCostsResultLimits,
})

FinanceSetPaymentCostsResultItem = TypedDict("FinanceSetPaymentCostsResultItem", {
    "provider": str,
    "name": str,
    "percent": float,
    "fixed": float,
})

TaxShowResultRatesItem = TypedDict("TaxShowResultRatesItem", {
    "country": str,
    "countryName": str,
    "region": str,
    "regionName": str,
    "rate": float,
    "label": str,
    "standard": float,
})

TaxShowResultStandardAT = TypedDict("TaxShowResultStandardAT", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardBE = TypedDict("TaxShowResultStandardBE", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardBG = TypedDict("TaxShowResultStandardBG", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardHR = TypedDict("TaxShowResultStandardHR", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardCY = TypedDict("TaxShowResultStandardCY", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardCZ = TypedDict("TaxShowResultStandardCZ", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardDK = TypedDict("TaxShowResultStandardDK", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardEE = TypedDict("TaxShowResultStandardEE", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardFI = TypedDict("TaxShowResultStandardFI", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardFR = TypedDict("TaxShowResultStandardFR", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardDE = TypedDict("TaxShowResultStandardDE", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardGR = TypedDict("TaxShowResultStandardGR", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardHU = TypedDict("TaxShowResultStandardHU", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardIE = TypedDict("TaxShowResultStandardIE", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardIT = TypedDict("TaxShowResultStandardIT", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardLV = TypedDict("TaxShowResultStandardLV", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardLT = TypedDict("TaxShowResultStandardLT", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardLU = TypedDict("TaxShowResultStandardLU", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardMT = TypedDict("TaxShowResultStandardMT", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardNL = TypedDict("TaxShowResultStandardNL", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardPL = TypedDict("TaxShowResultStandardPL", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardPT = TypedDict("TaxShowResultStandardPT", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardRO = TypedDict("TaxShowResultStandardRO", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardSK = TypedDict("TaxShowResultStandardSK", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardSI = TypedDict("TaxShowResultStandardSI", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardES = TypedDict("TaxShowResultStandardES", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardSE = TypedDict("TaxShowResultStandardSE", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardGB = TypedDict("TaxShowResultStandardGB", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardNO = TypedDict("TaxShowResultStandardNO", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardCH = TypedDict("TaxShowResultStandardCH", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardLI = TypedDict("TaxShowResultStandardLI", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardIS = TypedDict("TaxShowResultStandardIS", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardRS = TypedDict("TaxShowResultStandardRS", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardUA = TypedDict("TaxShowResultStandardUA", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardTR = TypedDict("TaxShowResultStandardTR", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardAU = TypedDict("TaxShowResultStandardAU", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardNZ = TypedDict("TaxShowResultStandardNZ", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardCA = TypedDict("TaxShowResultStandardCA", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardSG = TypedDict("TaxShowResultStandardSG", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardIN = TypedDict("TaxShowResultStandardIN", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardJP = TypedDict("TaxShowResultStandardJP", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardKR = TypedDict("TaxShowResultStandardKR", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardTW = TypedDict("TaxShowResultStandardTW", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardTH = TypedDict("TaxShowResultStandardTH", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardMY = TypedDict("TaxShowResultStandardMY", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardID = TypedDict("TaxShowResultStandardID", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardPH = TypedDict("TaxShowResultStandardPH", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardVN = TypedDict("TaxShowResultStandardVN", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardAE = TypedDict("TaxShowResultStandardAE", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardSA = TypedDict("TaxShowResultStandardSA", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardBH = TypedDict("TaxShowResultStandardBH", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardOM = TypedDict("TaxShowResultStandardOM", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardIL = TypedDict("TaxShowResultStandardIL", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardEG = TypedDict("TaxShowResultStandardEG", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardMA = TypedDict("TaxShowResultStandardMA", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardZA = TypedDict("TaxShowResultStandardZA", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardNG = TypedDict("TaxShowResultStandardNG", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardKE = TypedDict("TaxShowResultStandardKE", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardMX = TypedDict("TaxShowResultStandardMX", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardCL = TypedDict("TaxShowResultStandardCL", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardCO = TypedDict("TaxShowResultStandardCO", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardAR = TypedDict("TaxShowResultStandardAR", {
    "label": str,
    "rate": float,
})

TaxShowResultStandardPE = TypedDict("TaxShowResultStandardPE", {
    "label": str,
    "rate": float,
})

TaxShowResultStandard = TypedDict("TaxShowResultStandard", {
    "AT": TaxShowResultStandardAT,
    "BE": TaxShowResultStandardBE,
    "BG": TaxShowResultStandardBG,
    "HR": TaxShowResultStandardHR,
    "CY": TaxShowResultStandardCY,
    "CZ": TaxShowResultStandardCZ,
    "DK": TaxShowResultStandardDK,
    "EE": TaxShowResultStandardEE,
    "FI": TaxShowResultStandardFI,
    "FR": TaxShowResultStandardFR,
    "DE": TaxShowResultStandardDE,
    "GR": TaxShowResultStandardGR,
    "HU": TaxShowResultStandardHU,
    "IE": TaxShowResultStandardIE,
    "IT": TaxShowResultStandardIT,
    "LV": TaxShowResultStandardLV,
    "LT": TaxShowResultStandardLT,
    "LU": TaxShowResultStandardLU,
    "MT": TaxShowResultStandardMT,
    "NL": TaxShowResultStandardNL,
    "PL": TaxShowResultStandardPL,
    "PT": TaxShowResultStandardPT,
    "RO": TaxShowResultStandardRO,
    "SK": TaxShowResultStandardSK,
    "SI": TaxShowResultStandardSI,
    "ES": TaxShowResultStandardES,
    "SE": TaxShowResultStandardSE,
    "GB": TaxShowResultStandardGB,
    "NO": TaxShowResultStandardNO,
    "CH": TaxShowResultStandardCH,
    "LI": TaxShowResultStandardLI,
    "IS": TaxShowResultStandardIS,
    "RS": TaxShowResultStandardRS,
    "UA": TaxShowResultStandardUA,
    "TR": TaxShowResultStandardTR,
    "AU": TaxShowResultStandardAU,
    "NZ": TaxShowResultStandardNZ,
    "CA": TaxShowResultStandardCA,
    "SG": TaxShowResultStandardSG,
    "IN": TaxShowResultStandardIN,
    "JP": TaxShowResultStandardJP,
    "KR": TaxShowResultStandardKR,
    "TW": TaxShowResultStandardTW,
    "TH": TaxShowResultStandardTH,
    "MY": TaxShowResultStandardMY,
    "ID": TaxShowResultStandardID,
    "PH": TaxShowResultStandardPH,
    "VN": TaxShowResultStandardVN,
    "AE": TaxShowResultStandardAE,
    "SA": TaxShowResultStandardSA,
    "BH": TaxShowResultStandardBH,
    "OM": TaxShowResultStandardOM,
    "IL": TaxShowResultStandardIL,
    "EG": TaxShowResultStandardEG,
    "MA": TaxShowResultStandardMA,
    "ZA": TaxShowResultStandardZA,
    "NG": TaxShowResultStandardNG,
    "KE": TaxShowResultStandardKE,
    "MX": TaxShowResultStandardMX,
    "CL": TaxShowResultStandardCL,
    "CO": TaxShowResultStandardCO,
    "AR": TaxShowResultStandardAR,
    "PE": TaxShowResultStandardPE,
})

TaxShowResultRegionsUSItem = TypedDict("TaxShowResultRegionsUSItem", {
    "code": str,
    "name": str,
})

TaxShowResultRegions = TypedDict("TaxShowResultRegions", {
    "US": List[TaxShowResultRegionsUSItem],
})

TaxShowResult = TypedDict("TaxShowResult", {
    "collect": bool,
    "included": bool,
    "business": bool,
    "home": str,
    "homeName": str,
    "rates": List[TaxShowResultRatesItem],
    "standard": TaxShowResultStandard,
    "eu": List[str],
    "regions": TaxShowResultRegions,
    "limit": float,
    "maxRate": float,
})

TaxUpdateResultStandardAT = TypedDict("TaxUpdateResultStandardAT", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardBE = TypedDict("TaxUpdateResultStandardBE", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardBG = TypedDict("TaxUpdateResultStandardBG", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardHR = TypedDict("TaxUpdateResultStandardHR", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardCY = TypedDict("TaxUpdateResultStandardCY", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardCZ = TypedDict("TaxUpdateResultStandardCZ", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardDK = TypedDict("TaxUpdateResultStandardDK", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardEE = TypedDict("TaxUpdateResultStandardEE", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardFI = TypedDict("TaxUpdateResultStandardFI", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardFR = TypedDict("TaxUpdateResultStandardFR", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardDE = TypedDict("TaxUpdateResultStandardDE", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardGR = TypedDict("TaxUpdateResultStandardGR", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardHU = TypedDict("TaxUpdateResultStandardHU", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardIE = TypedDict("TaxUpdateResultStandardIE", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardIT = TypedDict("TaxUpdateResultStandardIT", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardLV = TypedDict("TaxUpdateResultStandardLV", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardLT = TypedDict("TaxUpdateResultStandardLT", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardLU = TypedDict("TaxUpdateResultStandardLU", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardMT = TypedDict("TaxUpdateResultStandardMT", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardNL = TypedDict("TaxUpdateResultStandardNL", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardPL = TypedDict("TaxUpdateResultStandardPL", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardPT = TypedDict("TaxUpdateResultStandardPT", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardRO = TypedDict("TaxUpdateResultStandardRO", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardSK = TypedDict("TaxUpdateResultStandardSK", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardSI = TypedDict("TaxUpdateResultStandardSI", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardES = TypedDict("TaxUpdateResultStandardES", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardSE = TypedDict("TaxUpdateResultStandardSE", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardGB = TypedDict("TaxUpdateResultStandardGB", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardNO = TypedDict("TaxUpdateResultStandardNO", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardCH = TypedDict("TaxUpdateResultStandardCH", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardLI = TypedDict("TaxUpdateResultStandardLI", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardIS = TypedDict("TaxUpdateResultStandardIS", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardRS = TypedDict("TaxUpdateResultStandardRS", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardUA = TypedDict("TaxUpdateResultStandardUA", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardTR = TypedDict("TaxUpdateResultStandardTR", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardAU = TypedDict("TaxUpdateResultStandardAU", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardNZ = TypedDict("TaxUpdateResultStandardNZ", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardCA = TypedDict("TaxUpdateResultStandardCA", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardSG = TypedDict("TaxUpdateResultStandardSG", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardIN = TypedDict("TaxUpdateResultStandardIN", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardJP = TypedDict("TaxUpdateResultStandardJP", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardKR = TypedDict("TaxUpdateResultStandardKR", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardTW = TypedDict("TaxUpdateResultStandardTW", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardTH = TypedDict("TaxUpdateResultStandardTH", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardMY = TypedDict("TaxUpdateResultStandardMY", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardID = TypedDict("TaxUpdateResultStandardID", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardPH = TypedDict("TaxUpdateResultStandardPH", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardVN = TypedDict("TaxUpdateResultStandardVN", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardAE = TypedDict("TaxUpdateResultStandardAE", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardSA = TypedDict("TaxUpdateResultStandardSA", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardBH = TypedDict("TaxUpdateResultStandardBH", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardOM = TypedDict("TaxUpdateResultStandardOM", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardIL = TypedDict("TaxUpdateResultStandardIL", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardEG = TypedDict("TaxUpdateResultStandardEG", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardMA = TypedDict("TaxUpdateResultStandardMA", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardZA = TypedDict("TaxUpdateResultStandardZA", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardNG = TypedDict("TaxUpdateResultStandardNG", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardKE = TypedDict("TaxUpdateResultStandardKE", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardMX = TypedDict("TaxUpdateResultStandardMX", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardCL = TypedDict("TaxUpdateResultStandardCL", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardCO = TypedDict("TaxUpdateResultStandardCO", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardAR = TypedDict("TaxUpdateResultStandardAR", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandardPE = TypedDict("TaxUpdateResultStandardPE", {
    "label": str,
    "rate": float,
})

TaxUpdateResultStandard = TypedDict("TaxUpdateResultStandard", {
    "AT": TaxUpdateResultStandardAT,
    "BE": TaxUpdateResultStandardBE,
    "BG": TaxUpdateResultStandardBG,
    "HR": TaxUpdateResultStandardHR,
    "CY": TaxUpdateResultStandardCY,
    "CZ": TaxUpdateResultStandardCZ,
    "DK": TaxUpdateResultStandardDK,
    "EE": TaxUpdateResultStandardEE,
    "FI": TaxUpdateResultStandardFI,
    "FR": TaxUpdateResultStandardFR,
    "DE": TaxUpdateResultStandardDE,
    "GR": TaxUpdateResultStandardGR,
    "HU": TaxUpdateResultStandardHU,
    "IE": TaxUpdateResultStandardIE,
    "IT": TaxUpdateResultStandardIT,
    "LV": TaxUpdateResultStandardLV,
    "LT": TaxUpdateResultStandardLT,
    "LU": TaxUpdateResultStandardLU,
    "MT": TaxUpdateResultStandardMT,
    "NL": TaxUpdateResultStandardNL,
    "PL": TaxUpdateResultStandardPL,
    "PT": TaxUpdateResultStandardPT,
    "RO": TaxUpdateResultStandardRO,
    "SK": TaxUpdateResultStandardSK,
    "SI": TaxUpdateResultStandardSI,
    "ES": TaxUpdateResultStandardES,
    "SE": TaxUpdateResultStandardSE,
    "GB": TaxUpdateResultStandardGB,
    "NO": TaxUpdateResultStandardNO,
    "CH": TaxUpdateResultStandardCH,
    "LI": TaxUpdateResultStandardLI,
    "IS": TaxUpdateResultStandardIS,
    "RS": TaxUpdateResultStandardRS,
    "UA": TaxUpdateResultStandardUA,
    "TR": TaxUpdateResultStandardTR,
    "AU": TaxUpdateResultStandardAU,
    "NZ": TaxUpdateResultStandardNZ,
    "CA": TaxUpdateResultStandardCA,
    "SG": TaxUpdateResultStandardSG,
    "IN": TaxUpdateResultStandardIN,
    "JP": TaxUpdateResultStandardJP,
    "KR": TaxUpdateResultStandardKR,
    "TW": TaxUpdateResultStandardTW,
    "TH": TaxUpdateResultStandardTH,
    "MY": TaxUpdateResultStandardMY,
    "ID": TaxUpdateResultStandardID,
    "PH": TaxUpdateResultStandardPH,
    "VN": TaxUpdateResultStandardVN,
    "AE": TaxUpdateResultStandardAE,
    "SA": TaxUpdateResultStandardSA,
    "BH": TaxUpdateResultStandardBH,
    "OM": TaxUpdateResultStandardOM,
    "IL": TaxUpdateResultStandardIL,
    "EG": TaxUpdateResultStandardEG,
    "MA": TaxUpdateResultStandardMA,
    "ZA": TaxUpdateResultStandardZA,
    "NG": TaxUpdateResultStandardNG,
    "KE": TaxUpdateResultStandardKE,
    "MX": TaxUpdateResultStandardMX,
    "CL": TaxUpdateResultStandardCL,
    "CO": TaxUpdateResultStandardCO,
    "AR": TaxUpdateResultStandardAR,
    "PE": TaxUpdateResultStandardPE,
})

TaxUpdateResultRegionsUSItem = TypedDict("TaxUpdateResultRegionsUSItem", {
    "code": str,
    "name": str,
})

TaxUpdateResultRegions = TypedDict("TaxUpdateResultRegions", {
    "US": List[TaxUpdateResultRegionsUSItem],
})

TaxUpdateResult = TypedDict("TaxUpdateResult", {
    "collect": bool,
    "included": bool,
    "business": bool,
    "home": str,
    "homeName": str,
    "rates": Union[List[Any], Dict[str, Any]],
    "standard": TaxUpdateResultStandard,
    "eu": List[str],
    "regions": TaxUpdateResultRegions,
    "limit": float,
    "maxRate": float,
})

TaxSetRatesResultRatesItem = TypedDict("TaxSetRatesResultRatesItem", {
    "country": str,
    "countryName": str,
    "region": str,
    "regionName": str,
    "rate": float,
    "label": str,
    "standard": float,
})

TaxSetRatesResultStandardAT = TypedDict("TaxSetRatesResultStandardAT", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardBE = TypedDict("TaxSetRatesResultStandardBE", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardBG = TypedDict("TaxSetRatesResultStandardBG", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardHR = TypedDict("TaxSetRatesResultStandardHR", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardCY = TypedDict("TaxSetRatesResultStandardCY", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardCZ = TypedDict("TaxSetRatesResultStandardCZ", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardDK = TypedDict("TaxSetRatesResultStandardDK", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardEE = TypedDict("TaxSetRatesResultStandardEE", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardFI = TypedDict("TaxSetRatesResultStandardFI", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardFR = TypedDict("TaxSetRatesResultStandardFR", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardDE = TypedDict("TaxSetRatesResultStandardDE", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardGR = TypedDict("TaxSetRatesResultStandardGR", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardHU = TypedDict("TaxSetRatesResultStandardHU", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardIE = TypedDict("TaxSetRatesResultStandardIE", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardIT = TypedDict("TaxSetRatesResultStandardIT", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardLV = TypedDict("TaxSetRatesResultStandardLV", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardLT = TypedDict("TaxSetRatesResultStandardLT", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardLU = TypedDict("TaxSetRatesResultStandardLU", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardMT = TypedDict("TaxSetRatesResultStandardMT", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardNL = TypedDict("TaxSetRatesResultStandardNL", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardPL = TypedDict("TaxSetRatesResultStandardPL", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardPT = TypedDict("TaxSetRatesResultStandardPT", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardRO = TypedDict("TaxSetRatesResultStandardRO", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardSK = TypedDict("TaxSetRatesResultStandardSK", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardSI = TypedDict("TaxSetRatesResultStandardSI", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardES = TypedDict("TaxSetRatesResultStandardES", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardSE = TypedDict("TaxSetRatesResultStandardSE", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardGB = TypedDict("TaxSetRatesResultStandardGB", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardNO = TypedDict("TaxSetRatesResultStandardNO", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardCH = TypedDict("TaxSetRatesResultStandardCH", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardLI = TypedDict("TaxSetRatesResultStandardLI", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardIS = TypedDict("TaxSetRatesResultStandardIS", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardRS = TypedDict("TaxSetRatesResultStandardRS", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardUA = TypedDict("TaxSetRatesResultStandardUA", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardTR = TypedDict("TaxSetRatesResultStandardTR", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardAU = TypedDict("TaxSetRatesResultStandardAU", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardNZ = TypedDict("TaxSetRatesResultStandardNZ", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardCA = TypedDict("TaxSetRatesResultStandardCA", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardSG = TypedDict("TaxSetRatesResultStandardSG", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardIN = TypedDict("TaxSetRatesResultStandardIN", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardJP = TypedDict("TaxSetRatesResultStandardJP", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardKR = TypedDict("TaxSetRatesResultStandardKR", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardTW = TypedDict("TaxSetRatesResultStandardTW", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardTH = TypedDict("TaxSetRatesResultStandardTH", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardMY = TypedDict("TaxSetRatesResultStandardMY", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardID = TypedDict("TaxSetRatesResultStandardID", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardPH = TypedDict("TaxSetRatesResultStandardPH", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardVN = TypedDict("TaxSetRatesResultStandardVN", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardAE = TypedDict("TaxSetRatesResultStandardAE", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardSA = TypedDict("TaxSetRatesResultStandardSA", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardBH = TypedDict("TaxSetRatesResultStandardBH", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardOM = TypedDict("TaxSetRatesResultStandardOM", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardIL = TypedDict("TaxSetRatesResultStandardIL", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardEG = TypedDict("TaxSetRatesResultStandardEG", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardMA = TypedDict("TaxSetRatesResultStandardMA", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardZA = TypedDict("TaxSetRatesResultStandardZA", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardNG = TypedDict("TaxSetRatesResultStandardNG", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardKE = TypedDict("TaxSetRatesResultStandardKE", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardMX = TypedDict("TaxSetRatesResultStandardMX", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardCL = TypedDict("TaxSetRatesResultStandardCL", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardCO = TypedDict("TaxSetRatesResultStandardCO", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardAR = TypedDict("TaxSetRatesResultStandardAR", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandardPE = TypedDict("TaxSetRatesResultStandardPE", {
    "label": str,
    "rate": float,
})

TaxSetRatesResultStandard = TypedDict("TaxSetRatesResultStandard", {
    "AT": TaxSetRatesResultStandardAT,
    "BE": TaxSetRatesResultStandardBE,
    "BG": TaxSetRatesResultStandardBG,
    "HR": TaxSetRatesResultStandardHR,
    "CY": TaxSetRatesResultStandardCY,
    "CZ": TaxSetRatesResultStandardCZ,
    "DK": TaxSetRatesResultStandardDK,
    "EE": TaxSetRatesResultStandardEE,
    "FI": TaxSetRatesResultStandardFI,
    "FR": TaxSetRatesResultStandardFR,
    "DE": TaxSetRatesResultStandardDE,
    "GR": TaxSetRatesResultStandardGR,
    "HU": TaxSetRatesResultStandardHU,
    "IE": TaxSetRatesResultStandardIE,
    "IT": TaxSetRatesResultStandardIT,
    "LV": TaxSetRatesResultStandardLV,
    "LT": TaxSetRatesResultStandardLT,
    "LU": TaxSetRatesResultStandardLU,
    "MT": TaxSetRatesResultStandardMT,
    "NL": TaxSetRatesResultStandardNL,
    "PL": TaxSetRatesResultStandardPL,
    "PT": TaxSetRatesResultStandardPT,
    "RO": TaxSetRatesResultStandardRO,
    "SK": TaxSetRatesResultStandardSK,
    "SI": TaxSetRatesResultStandardSI,
    "ES": TaxSetRatesResultStandardES,
    "SE": TaxSetRatesResultStandardSE,
    "GB": TaxSetRatesResultStandardGB,
    "NO": TaxSetRatesResultStandardNO,
    "CH": TaxSetRatesResultStandardCH,
    "LI": TaxSetRatesResultStandardLI,
    "IS": TaxSetRatesResultStandardIS,
    "RS": TaxSetRatesResultStandardRS,
    "UA": TaxSetRatesResultStandardUA,
    "TR": TaxSetRatesResultStandardTR,
    "AU": TaxSetRatesResultStandardAU,
    "NZ": TaxSetRatesResultStandardNZ,
    "CA": TaxSetRatesResultStandardCA,
    "SG": TaxSetRatesResultStandardSG,
    "IN": TaxSetRatesResultStandardIN,
    "JP": TaxSetRatesResultStandardJP,
    "KR": TaxSetRatesResultStandardKR,
    "TW": TaxSetRatesResultStandardTW,
    "TH": TaxSetRatesResultStandardTH,
    "MY": TaxSetRatesResultStandardMY,
    "ID": TaxSetRatesResultStandardID,
    "PH": TaxSetRatesResultStandardPH,
    "VN": TaxSetRatesResultStandardVN,
    "AE": TaxSetRatesResultStandardAE,
    "SA": TaxSetRatesResultStandardSA,
    "BH": TaxSetRatesResultStandardBH,
    "OM": TaxSetRatesResultStandardOM,
    "IL": TaxSetRatesResultStandardIL,
    "EG": TaxSetRatesResultStandardEG,
    "MA": TaxSetRatesResultStandardMA,
    "ZA": TaxSetRatesResultStandardZA,
    "NG": TaxSetRatesResultStandardNG,
    "KE": TaxSetRatesResultStandardKE,
    "MX": TaxSetRatesResultStandardMX,
    "CL": TaxSetRatesResultStandardCL,
    "CO": TaxSetRatesResultStandardCO,
    "AR": TaxSetRatesResultStandardAR,
    "PE": TaxSetRatesResultStandardPE,
})

TaxSetRatesResultRegionsUSItem = TypedDict("TaxSetRatesResultRegionsUSItem", {
    "code": str,
    "name": str,
})

TaxSetRatesResultRegions = TypedDict("TaxSetRatesResultRegions", {
    "US": List[TaxSetRatesResultRegionsUSItem],
})

TaxSetRatesResult = TypedDict("TaxSetRatesResult", {
    "collect": bool,
    "included": bool,
    "business": bool,
    "home": str,
    "homeName": str,
    "rates": List[TaxSetRatesResultRatesItem],
    "standard": TaxSetRatesResultStandard,
    "eu": List[str],
    "regions": TaxSetRatesResultRegions,
    "limit": float,
    "maxRate": float,
})

TaxDeleteRateResultRatesItem = TypedDict("TaxDeleteRateResultRatesItem", {
    "country": str,
    "countryName": str,
    "region": str,
    "regionName": str,
    "rate": float,
    "label": str,
    "standard": float,
})

TaxDeleteRateResultStandardAT = TypedDict("TaxDeleteRateResultStandardAT", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardBE = TypedDict("TaxDeleteRateResultStandardBE", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardBG = TypedDict("TaxDeleteRateResultStandardBG", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardHR = TypedDict("TaxDeleteRateResultStandardHR", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardCY = TypedDict("TaxDeleteRateResultStandardCY", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardCZ = TypedDict("TaxDeleteRateResultStandardCZ", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardDK = TypedDict("TaxDeleteRateResultStandardDK", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardEE = TypedDict("TaxDeleteRateResultStandardEE", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardFI = TypedDict("TaxDeleteRateResultStandardFI", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardFR = TypedDict("TaxDeleteRateResultStandardFR", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardDE = TypedDict("TaxDeleteRateResultStandardDE", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardGR = TypedDict("TaxDeleteRateResultStandardGR", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardHU = TypedDict("TaxDeleteRateResultStandardHU", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardIE = TypedDict("TaxDeleteRateResultStandardIE", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardIT = TypedDict("TaxDeleteRateResultStandardIT", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardLV = TypedDict("TaxDeleteRateResultStandardLV", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardLT = TypedDict("TaxDeleteRateResultStandardLT", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardLU = TypedDict("TaxDeleteRateResultStandardLU", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardMT = TypedDict("TaxDeleteRateResultStandardMT", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardNL = TypedDict("TaxDeleteRateResultStandardNL", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardPL = TypedDict("TaxDeleteRateResultStandardPL", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardPT = TypedDict("TaxDeleteRateResultStandardPT", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardRO = TypedDict("TaxDeleteRateResultStandardRO", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardSK = TypedDict("TaxDeleteRateResultStandardSK", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardSI = TypedDict("TaxDeleteRateResultStandardSI", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardES = TypedDict("TaxDeleteRateResultStandardES", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardSE = TypedDict("TaxDeleteRateResultStandardSE", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardGB = TypedDict("TaxDeleteRateResultStandardGB", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardNO = TypedDict("TaxDeleteRateResultStandardNO", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardCH = TypedDict("TaxDeleteRateResultStandardCH", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardLI = TypedDict("TaxDeleteRateResultStandardLI", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardIS = TypedDict("TaxDeleteRateResultStandardIS", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardRS = TypedDict("TaxDeleteRateResultStandardRS", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardUA = TypedDict("TaxDeleteRateResultStandardUA", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardTR = TypedDict("TaxDeleteRateResultStandardTR", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardAU = TypedDict("TaxDeleteRateResultStandardAU", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardNZ = TypedDict("TaxDeleteRateResultStandardNZ", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardCA = TypedDict("TaxDeleteRateResultStandardCA", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardSG = TypedDict("TaxDeleteRateResultStandardSG", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardIN = TypedDict("TaxDeleteRateResultStandardIN", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardJP = TypedDict("TaxDeleteRateResultStandardJP", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardKR = TypedDict("TaxDeleteRateResultStandardKR", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardTW = TypedDict("TaxDeleteRateResultStandardTW", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardTH = TypedDict("TaxDeleteRateResultStandardTH", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardMY = TypedDict("TaxDeleteRateResultStandardMY", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardID = TypedDict("TaxDeleteRateResultStandardID", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardPH = TypedDict("TaxDeleteRateResultStandardPH", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardVN = TypedDict("TaxDeleteRateResultStandardVN", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardAE = TypedDict("TaxDeleteRateResultStandardAE", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardSA = TypedDict("TaxDeleteRateResultStandardSA", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardBH = TypedDict("TaxDeleteRateResultStandardBH", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardOM = TypedDict("TaxDeleteRateResultStandardOM", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardIL = TypedDict("TaxDeleteRateResultStandardIL", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardEG = TypedDict("TaxDeleteRateResultStandardEG", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardMA = TypedDict("TaxDeleteRateResultStandardMA", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardZA = TypedDict("TaxDeleteRateResultStandardZA", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardNG = TypedDict("TaxDeleteRateResultStandardNG", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardKE = TypedDict("TaxDeleteRateResultStandardKE", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardMX = TypedDict("TaxDeleteRateResultStandardMX", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardCL = TypedDict("TaxDeleteRateResultStandardCL", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardCO = TypedDict("TaxDeleteRateResultStandardCO", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardAR = TypedDict("TaxDeleteRateResultStandardAR", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandardPE = TypedDict("TaxDeleteRateResultStandardPE", {
    "label": str,
    "rate": float,
})

TaxDeleteRateResultStandard = TypedDict("TaxDeleteRateResultStandard", {
    "AT": TaxDeleteRateResultStandardAT,
    "BE": TaxDeleteRateResultStandardBE,
    "BG": TaxDeleteRateResultStandardBG,
    "HR": TaxDeleteRateResultStandardHR,
    "CY": TaxDeleteRateResultStandardCY,
    "CZ": TaxDeleteRateResultStandardCZ,
    "DK": TaxDeleteRateResultStandardDK,
    "EE": TaxDeleteRateResultStandardEE,
    "FI": TaxDeleteRateResultStandardFI,
    "FR": TaxDeleteRateResultStandardFR,
    "DE": TaxDeleteRateResultStandardDE,
    "GR": TaxDeleteRateResultStandardGR,
    "HU": TaxDeleteRateResultStandardHU,
    "IE": TaxDeleteRateResultStandardIE,
    "IT": TaxDeleteRateResultStandardIT,
    "LV": TaxDeleteRateResultStandardLV,
    "LT": TaxDeleteRateResultStandardLT,
    "LU": TaxDeleteRateResultStandardLU,
    "MT": TaxDeleteRateResultStandardMT,
    "NL": TaxDeleteRateResultStandardNL,
    "PL": TaxDeleteRateResultStandardPL,
    "PT": TaxDeleteRateResultStandardPT,
    "RO": TaxDeleteRateResultStandardRO,
    "SK": TaxDeleteRateResultStandardSK,
    "SI": TaxDeleteRateResultStandardSI,
    "ES": TaxDeleteRateResultStandardES,
    "SE": TaxDeleteRateResultStandardSE,
    "GB": TaxDeleteRateResultStandardGB,
    "NO": TaxDeleteRateResultStandardNO,
    "CH": TaxDeleteRateResultStandardCH,
    "LI": TaxDeleteRateResultStandardLI,
    "IS": TaxDeleteRateResultStandardIS,
    "RS": TaxDeleteRateResultStandardRS,
    "UA": TaxDeleteRateResultStandardUA,
    "TR": TaxDeleteRateResultStandardTR,
    "AU": TaxDeleteRateResultStandardAU,
    "NZ": TaxDeleteRateResultStandardNZ,
    "CA": TaxDeleteRateResultStandardCA,
    "SG": TaxDeleteRateResultStandardSG,
    "IN": TaxDeleteRateResultStandardIN,
    "JP": TaxDeleteRateResultStandardJP,
    "KR": TaxDeleteRateResultStandardKR,
    "TW": TaxDeleteRateResultStandardTW,
    "TH": TaxDeleteRateResultStandardTH,
    "MY": TaxDeleteRateResultStandardMY,
    "ID": TaxDeleteRateResultStandardID,
    "PH": TaxDeleteRateResultStandardPH,
    "VN": TaxDeleteRateResultStandardVN,
    "AE": TaxDeleteRateResultStandardAE,
    "SA": TaxDeleteRateResultStandardSA,
    "BH": TaxDeleteRateResultStandardBH,
    "OM": TaxDeleteRateResultStandardOM,
    "IL": TaxDeleteRateResultStandardIL,
    "EG": TaxDeleteRateResultStandardEG,
    "MA": TaxDeleteRateResultStandardMA,
    "ZA": TaxDeleteRateResultStandardZA,
    "NG": TaxDeleteRateResultStandardNG,
    "KE": TaxDeleteRateResultStandardKE,
    "MX": TaxDeleteRateResultStandardMX,
    "CL": TaxDeleteRateResultStandardCL,
    "CO": TaxDeleteRateResultStandardCO,
    "AR": TaxDeleteRateResultStandardAR,
    "PE": TaxDeleteRateResultStandardPE,
})

TaxDeleteRateResultRegionsUSItem = TypedDict("TaxDeleteRateResultRegionsUSItem", {
    "code": str,
    "name": str,
})

TaxDeleteRateResultRegions = TypedDict("TaxDeleteRateResultRegions", {
    "US": List[TaxDeleteRateResultRegionsUSItem],
})

TaxDeleteRateResult = TypedDict("TaxDeleteRateResult", {
    "collect": bool,
    "included": bool,
    "business": bool,
    "home": str,
    "homeName": str,
    "rates": List[TaxDeleteRateResultRatesItem],
    "standard": TaxDeleteRateResultStandard,
    "eu": List[str],
    "regions": TaxDeleteRateResultRegions,
    "limit": float,
    "maxRate": float,
})

ExpensesListResultItemCategory = TypedDict("ExpensesListResultItemCategory", {
    "id": str,
    "name": str,
    "icon": str,
})

ExpensesListResultItem = TypedDict("ExpensesListResultItem", {
    "id": str,
    "spentOn": str,
    "payee": str,
    "note": str,
    "category": ExpensesListResultItemCategory,
    "method": str,
    "reference": str,
    "amount": float,
    "entered": Any,
    "productId": Any,
    "recurring": bool,
    "source": str,
    "receipt": Any,
    "createdAt": str,
    "updatedAt": str,
})

ExpensesCreateResultCategory = TypedDict("ExpensesCreateResultCategory", {
    "id": str,
    "name": str,
    "icon": str,
})

ExpensesCreateResult = TypedDict("ExpensesCreateResult", {
    "id": str,
    "spentOn": str,
    "payee": str,
    "note": str,
    "category": ExpensesCreateResultCategory,
    "method": str,
    "reference": str,
    "amount": float,
    "entered": Any,
    "productId": Any,
    "recurring": bool,
    "source": str,
    "receipt": Any,
    "createdAt": str,
    "updatedAt": str,
})

ExpensesSummaryResultPeriod = TypedDict("ExpensesSummaryResultPeriod", {
    "from": str,
    "to": str,
    "label": str,
    "previousFrom": str,
    "previousTo": str,
    "previousLabel": str,
})

ExpensesSummaryResultRecurring = TypedDict("ExpensesSummaryResultRecurring", {
    "count": float,
    "monthly": float,
})

ExpensesSummaryResultLargest = TypedDict("ExpensesSummaryResultLargest", {
    "name": str,
    "icon": str,
    "total": float,
    "share": float,
})

ExpensesSummaryResultReceipts = TypedDict("ExpensesSummaryResultReceipts", {
    "attached": float,
    "total": float,
})

ExpensesSummaryResultMonthsItem = TypedDict("ExpensesSummaryResultMonthsItem", {
    "month": str,
    "total": float,
})

ExpensesSummaryResultCounts = TypedDict("ExpensesSummaryResultCounts", {
    "recurring": float,
    "rules": float,
})

ExpensesSummaryResult = TypedDict("ExpensesSummaryResult", {
    "period": ExpensesSummaryResultPeriod,
    "spent": float,
    "previous": float,
    "recurring": ExpensesSummaryResultRecurring,
    "largest": ExpensesSummaryResultLargest,
    "receipts": ExpensesSummaryResultReceipts,
    "months": List[ExpensesSummaryResultMonthsItem],
    "comingUp": Union[List[Any], Dict[str, Any]],
    "counts": ExpensesSummaryResultCounts,
})

ExpensesSetupResultCategoriesItem = TypedDict("ExpensesSetupResultCategoriesItem", {
    "id": str,
    "name": str,
    "icon": str,
    "updatedAt": str,
})

ExpensesSetupResultPayeesItem = TypedDict("ExpensesSetupResultPayeesItem", {
    "payee": str,
    "categoryId": str,
    "method": str,
})

ExpensesSetupResultMethodsItem = TypedDict("ExpensesSetupResultMethodsItem", {
    "key": str,
    "name": str,
})

ExpensesSetupResultReceipts = TypedDict("ExpensesSetupResultReceipts", {
    "enabled": bool,
    "maxSize": float,
    "types": List[str],
})

ExpensesSetupResultLimits = TypedDict("ExpensesSetupResultLimits", {
    "categories": float,
    "recurring": float,
    "rules": float,
    "importRows": float,
    "payee": float,
    "note": float,
    "reference": float,
    "amount": float,
    "category": float,
    "phrase": float,
})

ExpensesSetupResult = TypedDict("ExpensesSetupResult", {
    "currency": str,
    "currencies": Union[List[Any], Dict[str, Any]],
    "categories": List[ExpensesSetupResultCategoriesItem],
    "icons": List[str],
    "payees": List[ExpensesSetupResultPayeesItem],
    "methods": List[ExpensesSetupResultMethodsItem],
    "receipts": ExpensesSetupResultReceipts,
    "limits": ExpensesSetupResultLimits,
})

ExpensesUpdateResultCategory = TypedDict("ExpensesUpdateResultCategory", {
    "id": str,
    "name": str,
    "icon": str,
})

ExpensesUpdateResult = TypedDict("ExpensesUpdateResult", {
    "id": str,
    "spentOn": str,
    "payee": str,
    "note": str,
    "category": ExpensesUpdateResultCategory,
    "method": str,
    "reference": str,
    "amount": float,
    "entered": Any,
    "productId": Any,
    "recurring": bool,
    "source": str,
    "receipt": Any,
    "createdAt": str,
    "updatedAt": str,
})

ExpensesDeleteResult = TypedDict("ExpensesDeleteResult", {
    "id": str,
    "deleted": bool,
})

ExpenseCategoriesListResultItem = TypedDict("ExpenseCategoriesListResultItem", {
    "id": str,
    "name": str,
    "icon": str,
    "updatedAt": str,
})

ExpenseCategoriesCreateResult = TypedDict("ExpenseCategoriesCreateResult", {
    "id": str,
    "name": str,
    "icon": str,
    "updatedAt": str,
})

ExpenseCategoriesUpdateResult = TypedDict("ExpenseCategoriesUpdateResult", {
    "id": str,
    "name": str,
    "icon": str,
    "updatedAt": str,
})

ExpenseCategoriesDeleteResult = TypedDict("ExpenseCategoriesDeleteResult", {
    "id": str,
    "deleted": bool,
    "moved": float,
})

ExpenseCategoriesSortResult = TypedDict("ExpenseCategoriesSortResult", {
    "reordered": float,
})

RecurringExpensesListResultItem = TypedDict("RecurringExpensesListResultItem", {
    "id": str,
    "payee": str,
    "note": str,
    "category": Any,
    "method": str,
    "reference": str,
    "amount": float,
    "cadence": str,
    "onDay": float,
    "nextOn": str,
    "asks": bool,
    "paused": bool,
    "waiting": bool,
    "updatedAt": str,
})

RecurringExpensesCreateResult = TypedDict("RecurringExpensesCreateResult", {
    "id": str,
    "payee": str,
    "note": str,
    "category": Any,
    "method": str,
    "reference": str,
    "amount": float,
    "cadence": str,
    "onDay": float,
    "nextOn": str,
    "asks": bool,
    "paused": bool,
    "waiting": bool,
    "updatedAt": str,
})

RecurringExpensesUpdateResult = TypedDict("RecurringExpensesUpdateResult", {
    "id": str,
    "payee": str,
    "note": str,
    "category": Any,
    "method": str,
    "reference": str,
    "amount": float,
    "cadence": str,
    "onDay": float,
    "nextOn": str,
    "asks": bool,
    "paused": bool,
    "waiting": bool,
    "updatedAt": str,
})

RecurringExpensesDeleteResult = TypedDict("RecurringExpensesDeleteResult", {
    "id": str,
    "deleted": bool,
})

RecurringExpensesSkipResultRecurring = TypedDict("RecurringExpensesSkipResultRecurring", {
    "id": str,
    "payee": str,
    "note": str,
    "category": Any,
    "method": str,
    "reference": str,
    "amount": float,
    "cadence": str,
    "onDay": float,
    "nextOn": str,
    "asks": bool,
    "paused": bool,
    "waiting": bool,
    "updatedAt": str,
})

RecurringExpensesSkipResult = TypedDict("RecurringExpensesSkipResult", {
    "recurring": RecurringExpensesSkipResultRecurring,
    "expense": Any,
})

ExpenseRulesListResultItemCategory = TypedDict("ExpenseRulesListResultItemCategory", {
    "id": str,
    "name": str,
    "icon": str,
})

ExpenseRulesListResultItem = TypedDict("ExpenseRulesListResultItem", {
    "id": str,
    "phrase": str,
    "category": ExpenseRulesListResultItemCategory,
})

ExpenseRulesCreateResultCategory = TypedDict("ExpenseRulesCreateResultCategory", {
    "id": str,
    "name": str,
    "icon": str,
})

ExpenseRulesCreateResult = TypedDict("ExpenseRulesCreateResult", {
    "id": str,
    "phrase": str,
    "category": ExpenseRulesCreateResultCategory,
})

ExpenseRulesDeleteResult = TypedDict("ExpenseRulesDeleteResult", {
    "id": str,
    "deleted": bool,
})

RequestsListItemApiKey = TypedDict("RequestsListItemApiKey", {
    "id": str,
    "name": str,
    "prefix": str,
})

RequestsListItem = TypedDict("RequestsListItem", {
    "id": str,
    "method": str,
    "path": str,
    "query": str,
    "operation": str,
    "status": float,
    "code": Any,
    "durationMs": float,
    "ip": str,
    "userAgent": str,
    "apiKey": RequestsListItemApiKey,
    "createdAt": str,
})

RequestsShowResultApiKey = TypedDict("RequestsShowResultApiKey", {
    "id": str,
    "name": str,
    "prefix": str,
})

RequestsShowResult = TypedDict("RequestsShowResult", {
    "id": str,
    "method": str,
    "path": str,
    "query": str,
    "operation": str,
    "status": float,
    "code": Any,
    "durationMs": float,
    "ip": str,
    "userAgent": str,
    "apiKey": RequestsShowResultApiKey,
    "createdAt": str,
    "requestBody": Any,
    "responseBody": str,
})

WebhooksListResultItem = TypedDict("WebhooksListResultItem", {
    "id": str,
    "url": str,
    "description": str,
    "events": List[str],
    "enabled": bool,
    "pausedAt": Any,
    "failures": float,
    "lastDeliveryAt": Any,
    "lastStatus": Any,
    "dateCreated": str,
    "updatedAt": str,
    "recentDeliveries": Union[List[Any], Dict[str, Any]],
})

WebhooksCreateResult = TypedDict("WebhooksCreateResult", {
    "id": str,
    "url": str,
    "description": str,
    "events": List[str],
    "enabled": bool,
    "pausedAt": Any,
    "failures": float,
    "lastDeliveryAt": Any,
    "lastStatus": Any,
    "dateCreated": str,
    "updatedAt": str,
    "secret": str,
})

WebhooksShowResult = TypedDict("WebhooksShowResult", {
    "id": str,
    "url": str,
    "description": str,
    "events": List[str],
    "enabled": bool,
    "pausedAt": Any,
    "failures": float,
    "lastDeliveryAt": Any,
    "lastStatus": Any,
    "dateCreated": str,
    "updatedAt": str,
})

WebhooksUpdateResult = TypedDict("WebhooksUpdateResult", {
    "id": str,
    "url": str,
    "description": str,
    "events": List[str],
    "enabled": bool,
    "pausedAt": Any,
    "failures": float,
    "lastDeliveryAt": Any,
    "lastStatus": Any,
    "dateCreated": str,
    "updatedAt": str,
})

WebhooksDeleteResult = TypedDict("WebhooksDeleteResult", {
    "id": str,
    "deleted": bool,
})

CustomerOrdersShowResultLinesItemDelivery = TypedDict("CustomerOrdersShowResultLinesItemDelivery", {
    "keys": List[str],
    "previousKeys": Union[List[Any], Dict[str, Any]],
    "items": Union[List[Any], Dict[str, Any]],
    "previousItems": Union[List[Any], Dict[str, Any]],
    "state": str,
    "message": str,
    "instructions": str,
    "files": Union[List[Any], Dict[str, Any]],
})

CustomerOrdersShowResultLinesItem = TypedDict("CustomerOrdersShowResultLinesItem", {
    "productName": str,
    "variantName": str,
    "quantity": float,
    "lineTotal": float,
    "imageUrl": Any,
    "productPath": str,
    "delivery": CustomerOrdersShowResultLinesItemDelivery,
})

CustomerOrdersShowResult = TypedDict("CustomerOrdersShowResult", {
    "id": str,
    "status": str,
    "dateCreated": str,
    "paidAt": str,
    "paidWith": str,
    "currencyCode": str,
    "shopCurrency": str,
    "subtotal": float,
    "discount": float,
    "fee": float,
    "tax": Any,
    "total": float,
    "couponCode": str,
    "checkoutUrl": str,
    "lines": List[CustomerOrdersShowResultLinesItem],
    "general": str,
})

CustomerAffiliatePayoutsCreateResultOffered = TypedDict("CustomerAffiliatePayoutsCreateResultOffered", {
    "commission": float,
    "discount": float,
})

CustomerAffiliatePayoutsCreateResultEarned = TypedDict("CustomerAffiliatePayoutsCreateResultEarned", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliatePayoutsCreateResultBalance = TypedDict("CustomerAffiliatePayoutsCreateResultBalance", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliatePayoutsCreateResultPaidOut = TypedDict("CustomerAffiliatePayoutsCreateResultPaidOut", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliatePayoutsCreateResultCan = TypedDict("CustomerAffiliatePayoutsCreateResultCan", {
    "editLink": bool,
    "toStore": bool,
    "payouts": bool,
})

CustomerAffiliatePayoutsCreateResultPayout = TypedDict("CustomerAffiliatePayoutsCreateResultPayout", {
    "id": str,
    "amount": float,
    "currencyCode": str,
    "details": str,
    "status": str,
    "note": str,
    "dateRequested": str,
    "dateResolved": Any,
})

CustomerAffiliatePayoutsCreateResultPayoutsItem = TypedDict("CustomerAffiliatePayoutsCreateResultPayoutsItem", {
    "id": str,
    "amount": float,
    "currencyCode": str,
    "details": str,
    "status": str,
    "note": str,
    "dateRequested": str,
    "dateResolved": Any,
})

CustomerAffiliatePayoutsCreateResultChangesItem = TypedDict("CustomerAffiliatePayoutsCreateResultChangesItem", {
    "id": str,
    "kind": str,
    "amount": float,
    "balanceAfter": float,
    "currencyCode": str,
    "dateCreated": str,
})

CustomerAffiliatePayoutsCreateResultLimits = TypedDict("CustomerAffiliatePayoutsCreateResultLimits", {
    "codeMin": float,
    "codeMax": float,
    "details": float,
})

CustomerAffiliatePayoutsCreateResult = TypedDict("CustomerAffiliatePayoutsCreateResult", {
    "member": bool,
    "canJoin": bool,
    "offered": CustomerAffiliatePayoutsCreateResultOffered,
    "active": bool,
    "code": str,
    "link": str,
    "linkStart": str,
    "commission": float,
    "discount": float,
    "clicks": float,
    "orders": float,
    "earned": CustomerAffiliatePayoutsCreateResultEarned,
    "balance": CustomerAffiliatePayoutsCreateResultBalance,
    "paidOut": CustomerAffiliatePayoutsCreateResultPaidOut,
    "can": CustomerAffiliatePayoutsCreateResultCan,
    "payout": CustomerAffiliatePayoutsCreateResultPayout,
    "payouts": List[CustomerAffiliatePayoutsCreateResultPayoutsItem],
    "changes": List[CustomerAffiliatePayoutsCreateResultChangesItem],
    "limits": CustomerAffiliatePayoutsCreateResultLimits,
})

CustomerAffiliatePayoutsCancelResultOffered = TypedDict("CustomerAffiliatePayoutsCancelResultOffered", {
    "commission": float,
    "discount": float,
})

CustomerAffiliatePayoutsCancelResultEarned = TypedDict("CustomerAffiliatePayoutsCancelResultEarned", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliatePayoutsCancelResultBalance = TypedDict("CustomerAffiliatePayoutsCancelResultBalance", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliatePayoutsCancelResultPaidOut = TypedDict("CustomerAffiliatePayoutsCancelResultPaidOut", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliatePayoutsCancelResultCan = TypedDict("CustomerAffiliatePayoutsCancelResultCan", {
    "editLink": bool,
    "toStore": bool,
    "payouts": bool,
})

CustomerAffiliatePayoutsCancelResultPayoutsItem = TypedDict("CustomerAffiliatePayoutsCancelResultPayoutsItem", {
    "id": str,
    "amount": float,
    "currencyCode": str,
    "details": str,
    "status": str,
    "note": str,
    "dateRequested": str,
    "dateResolved": str,
})

CustomerAffiliatePayoutsCancelResultChangesItem = TypedDict("CustomerAffiliatePayoutsCancelResultChangesItem", {
    "id": str,
    "kind": str,
    "amount": float,
    "balanceAfter": float,
    "currencyCode": str,
    "dateCreated": str,
})

CustomerAffiliatePayoutsCancelResultLimits = TypedDict("CustomerAffiliatePayoutsCancelResultLimits", {
    "codeMin": float,
    "codeMax": float,
    "details": float,
})

CustomerAffiliatePayoutsCancelResult = TypedDict("CustomerAffiliatePayoutsCancelResult", {
    "member": bool,
    "canJoin": bool,
    "offered": CustomerAffiliatePayoutsCancelResultOffered,
    "active": bool,
    "code": str,
    "link": str,
    "linkStart": str,
    "commission": float,
    "discount": float,
    "clicks": float,
    "orders": float,
    "earned": CustomerAffiliatePayoutsCancelResultEarned,
    "balance": CustomerAffiliatePayoutsCancelResultBalance,
    "paidOut": CustomerAffiliatePayoutsCancelResultPaidOut,
    "can": CustomerAffiliatePayoutsCancelResultCan,
    "payout": Any,
    "payouts": List[CustomerAffiliatePayoutsCancelResultPayoutsItem],
    "changes": List[CustomerAffiliatePayoutsCancelResultChangesItem],
    "limits": CustomerAffiliatePayoutsCancelResultLimits,
})

CustomerAffiliateShowResultOffered = TypedDict("CustomerAffiliateShowResultOffered", {
    "commission": float,
    "discount": float,
})

CustomerAffiliateShowResultEarned = TypedDict("CustomerAffiliateShowResultEarned", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliateShowResultBalance = TypedDict("CustomerAffiliateShowResultBalance", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliateShowResultPaidOut = TypedDict("CustomerAffiliateShowResultPaidOut", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliateShowResultCan = TypedDict("CustomerAffiliateShowResultCan", {
    "editLink": bool,
    "toStore": bool,
    "payouts": bool,
})

CustomerAffiliateShowResultChangesItem = TypedDict("CustomerAffiliateShowResultChangesItem", {
    "id": str,
    "kind": str,
    "amount": float,
    "balanceAfter": float,
    "currencyCode": str,
    "dateCreated": str,
})

CustomerAffiliateShowResultLimits = TypedDict("CustomerAffiliateShowResultLimits", {
    "codeMin": float,
    "codeMax": float,
    "details": float,
})

CustomerAffiliateShowResult = TypedDict("CustomerAffiliateShowResult", {
    "member": bool,
    "canJoin": bool,
    "offered": CustomerAffiliateShowResultOffered,
    "active": bool,
    "code": str,
    "link": str,
    "linkStart": str,
    "commission": float,
    "discount": float,
    "clicks": float,
    "orders": float,
    "earned": CustomerAffiliateShowResultEarned,
    "balance": CustomerAffiliateShowResultBalance,
    "paidOut": CustomerAffiliateShowResultPaidOut,
    "can": CustomerAffiliateShowResultCan,
    "payout": Any,
    "payouts": Union[List[Any], Dict[str, Any]],
    "changes": List[CustomerAffiliateShowResultChangesItem],
    "limits": CustomerAffiliateShowResultLimits,
})

CustomerAffiliateJoinResultOffered = TypedDict("CustomerAffiliateJoinResultOffered", {
    "commission": float,
    "discount": float,
})

CustomerAffiliateJoinResultEarned = TypedDict("CustomerAffiliateJoinResultEarned", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliateJoinResultBalance = TypedDict("CustomerAffiliateJoinResultBalance", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliateJoinResultPaidOut = TypedDict("CustomerAffiliateJoinResultPaidOut", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliateJoinResultCan = TypedDict("CustomerAffiliateJoinResultCan", {
    "editLink": bool,
    "toStore": bool,
    "payouts": bool,
})

CustomerAffiliateJoinResultLimits = TypedDict("CustomerAffiliateJoinResultLimits", {
    "codeMin": float,
    "codeMax": float,
    "details": float,
})

CustomerAffiliateJoinResult = TypedDict("CustomerAffiliateJoinResult", {
    "member": bool,
    "canJoin": bool,
    "offered": CustomerAffiliateJoinResultOffered,
    "active": bool,
    "code": str,
    "link": str,
    "linkStart": str,
    "commission": float,
    "discount": float,
    "clicks": float,
    "orders": float,
    "earned": CustomerAffiliateJoinResultEarned,
    "balance": CustomerAffiliateJoinResultBalance,
    "paidOut": CustomerAffiliateJoinResultPaidOut,
    "can": CustomerAffiliateJoinResultCan,
    "payout": Any,
    "payouts": Union[List[Any], Dict[str, Any]],
    "changes": Union[List[Any], Dict[str, Any]],
    "limits": CustomerAffiliateJoinResultLimits,
})

CustomerAffiliateLinkResultOffered = TypedDict("CustomerAffiliateLinkResultOffered", {
    "commission": float,
    "discount": float,
})

CustomerAffiliateLinkResultEarned = TypedDict("CustomerAffiliateLinkResultEarned", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliateLinkResultBalance = TypedDict("CustomerAffiliateLinkResultBalance", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliateLinkResultPaidOut = TypedDict("CustomerAffiliateLinkResultPaidOut", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliateLinkResultCan = TypedDict("CustomerAffiliateLinkResultCan", {
    "editLink": bool,
    "toStore": bool,
    "payouts": bool,
})

CustomerAffiliateLinkResultChangesItem = TypedDict("CustomerAffiliateLinkResultChangesItem", {
    "id": str,
    "kind": str,
    "amount": float,
    "balanceAfter": float,
    "currencyCode": str,
    "dateCreated": str,
})

CustomerAffiliateLinkResultLimits = TypedDict("CustomerAffiliateLinkResultLimits", {
    "codeMin": float,
    "codeMax": float,
    "details": float,
})

CustomerAffiliateLinkResult = TypedDict("CustomerAffiliateLinkResult", {
    "member": bool,
    "canJoin": bool,
    "offered": CustomerAffiliateLinkResultOffered,
    "active": bool,
    "code": str,
    "link": str,
    "linkStart": str,
    "commission": float,
    "discount": float,
    "clicks": float,
    "orders": float,
    "earned": CustomerAffiliateLinkResultEarned,
    "balance": CustomerAffiliateLinkResultBalance,
    "paidOut": CustomerAffiliateLinkResultPaidOut,
    "can": CustomerAffiliateLinkResultCan,
    "payout": Any,
    "payouts": Union[List[Any], Dict[str, Any]],
    "changes": List[CustomerAffiliateLinkResultChangesItem],
    "limits": CustomerAffiliateLinkResultLimits,
})

CustomerAffiliateToStoreResultOffered = TypedDict("CustomerAffiliateToStoreResultOffered", {
    "commission": float,
    "discount": float,
})

CustomerAffiliateToStoreResultEarned = TypedDict("CustomerAffiliateToStoreResultEarned", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliateToStoreResultBalance = TypedDict("CustomerAffiliateToStoreResultBalance", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliateToStoreResultPaidOut = TypedDict("CustomerAffiliateToStoreResultPaidOut", {
    "amount": float,
    "currencyCode": str,
})

CustomerAffiliateToStoreResultCan = TypedDict("CustomerAffiliateToStoreResultCan", {
    "editLink": bool,
    "toStore": bool,
    "payouts": bool,
})

CustomerAffiliateToStoreResultPayoutsItem = TypedDict("CustomerAffiliateToStoreResultPayoutsItem", {
    "id": str,
    "amount": float,
    "currencyCode": str,
    "details": str,
    "status": str,
    "note": str,
    "dateRequested": str,
    "dateResolved": str,
})

CustomerAffiliateToStoreResultChangesItem = TypedDict("CustomerAffiliateToStoreResultChangesItem", {
    "id": str,
    "kind": str,
    "amount": float,
    "balanceAfter": float,
    "currencyCode": str,
    "dateCreated": str,
})

CustomerAffiliateToStoreResultLimits = TypedDict("CustomerAffiliateToStoreResultLimits", {
    "codeMin": float,
    "codeMax": float,
    "details": float,
})

CustomerAffiliateToStoreResult = TypedDict("CustomerAffiliateToStoreResult", {
    "member": bool,
    "canJoin": bool,
    "offered": CustomerAffiliateToStoreResultOffered,
    "active": bool,
    "code": str,
    "link": str,
    "linkStart": str,
    "commission": float,
    "discount": float,
    "clicks": float,
    "orders": float,
    "earned": CustomerAffiliateToStoreResultEarned,
    "balance": CustomerAffiliateToStoreResultBalance,
    "paidOut": CustomerAffiliateToStoreResultPaidOut,
    "can": CustomerAffiliateToStoreResultCan,
    "payout": Any,
    "payouts": List[CustomerAffiliateToStoreResultPayoutsItem],
    "changes": List[CustomerAffiliateToStoreResultChangesItem],
    "limits": CustomerAffiliateToStoreResultLimits,
})

CustomerSubscriptionsListResultItem = TypedDict("CustomerSubscriptionsListResultItem", {
    "id": str,
    "email": str,
    "productName": str,
    "variantName": str,
    "quantity": float,
    "price": float,
    "currency": str,
    "every": float,
    "unit": str,
    "status": str,
    "periodEnd": str,
    "graceEnd": Any,
    "renewalOrderId": str,
    "renewalUrl": str,
    "firstOrderId": str,
    "endedAt": Any,
    "revoked": bool,
    "pausedAt": Any,
    "resumeAt": Any,
    "pausedBy": Any,
    "renewsWith": Any,
    "autoRenews": bool,
    "chargeTried": float,
    "chargeNextAt": Any,
    "createdAt": str,
    "pausesLeft": float,
})

CustomerSubscriptionsCancelResultItem = TypedDict("CustomerSubscriptionsCancelResultItem", {
    "id": str,
    "email": str,
    "productName": str,
    "variantName": str,
    "quantity": float,
    "price": float,
    "currency": str,
    "every": float,
    "unit": str,
    "status": str,
    "periodEnd": str,
    "graceEnd": Any,
    "renewalOrderId": Any,
    "renewalUrl": Any,
    "firstOrderId": str,
    "endedAt": Any,
    "revoked": bool,
    "pausedAt": Any,
    "resumeAt": Any,
    "pausedBy": Any,
    "renewsWith": Any,
    "autoRenews": bool,
    "chargeTried": float,
    "chargeNextAt": Any,
    "createdAt": str,
    "pausesLeft": float,
})

CustomerSubscriptionsUndoResultItem = TypedDict("CustomerSubscriptionsUndoResultItem", {
    "id": str,
    "email": str,
    "productName": str,
    "variantName": str,
    "quantity": float,
    "price": float,
    "currency": str,
    "every": float,
    "unit": str,
    "status": str,
    "periodEnd": str,
    "graceEnd": Any,
    "renewalOrderId": Any,
    "renewalUrl": Any,
    "firstOrderId": str,
    "endedAt": Any,
    "revoked": bool,
    "pausedAt": Any,
    "resumeAt": Any,
    "pausedBy": Any,
    "renewsWith": Any,
    "autoRenews": bool,
    "chargeTried": float,
    "chargeNextAt": Any,
    "createdAt": str,
    "pausesLeft": float,
})

CustomerSubscriptionsPauseResultItem = TypedDict("CustomerSubscriptionsPauseResultItem", {
    "id": str,
    "email": str,
    "productName": str,
    "variantName": str,
    "quantity": float,
    "price": float,
    "currency": str,
    "every": float,
    "unit": str,
    "status": str,
    "periodEnd": str,
    "graceEnd": Any,
    "renewalOrderId": Any,
    "renewalUrl": Any,
    "firstOrderId": str,
    "endedAt": Any,
    "revoked": bool,
    "pausedAt": str,
    "resumeAt": str,
    "pausedBy": str,
    "renewsWith": Any,
    "autoRenews": bool,
    "chargeTried": float,
    "chargeNextAt": Any,
    "createdAt": str,
    "pausesLeft": float,
})

CustomerSubscriptionsResumeResultItem = TypedDict("CustomerSubscriptionsResumeResultItem", {
    "id": str,
    "email": str,
    "productName": str,
    "variantName": str,
    "quantity": float,
    "price": float,
    "currency": str,
    "every": float,
    "unit": str,
    "status": str,
    "periodEnd": str,
    "graceEnd": Any,
    "renewalOrderId": Any,
    "renewalUrl": Any,
    "firstOrderId": str,
    "endedAt": Any,
    "revoked": bool,
    "pausedAt": Any,
    "resumeAt": Any,
    "pausedBy": Any,
    "renewsWith": Any,
    "autoRenews": bool,
    "chargeTried": float,
    "chargeNextAt": Any,
    "createdAt": str,
    "pausesLeft": float,
})

CustomerLoginResult = TypedDict("CustomerLoginResult", {
    "email": str,
    "resendIn": float,
    "expiresIn": float,
})

CustomerVerifyResult = TypedDict("CustomerVerifyResult", {
    "token": str,
    "tokenType": str,
    "expiresAt": str,
    "email": str,
})

CustomerShowResultAffiliate = TypedDict("CustomerShowResultAffiliate", {
    "member": bool,
    "canJoin": bool,
})

CustomerShowResultTotalsSpentItem = TypedDict("CustomerShowResultTotalsSpentItem", {
    "currencyCode": str,
    "amount": float,
})

CustomerShowResultTotals = TypedDict("CustomerShowResultTotals", {
    "spent": List[CustomerShowResultTotalsSpentItem],
    "orders": float,
    "keys": float,
})

CustomerShowResultOrdersItem = TypedDict("CustomerShowResultOrdersItem", {
    "id": str,
    "status": str,
    "dateCreated": str,
    "currencyCode": str,
    "total": float,
    "productName": str,
    "variantName": str,
    "quantity": float,
    "moreItems": float,
    "imageUrl": Any,
})

CustomerShowResultDownloads = TypedDict("CustomerShowResultDownloads", {
    "buttons": Union[List[Any], Dict[str, Any]],
    "guideUrl": str,
    "files": Union[List[Any], Dict[str, Any]],
    "instructions": Union[List[Any], Dict[str, Any]],
    "general": str,
})

CustomerShowResult = TypedDict("CustomerShowResult", {
    "email": str,
    "customerSince": str,
    "balance": Any,
    "affiliate": CustomerShowResultAffiliate,
    "totals": CustomerShowResultTotals,
    "orders": List[CustomerShowResultOrdersItem],
    "subscriptions": bool,
    "downloads": CustomerShowResultDownloads,
    "supportUrl": str,
})

CustomerLogoutResult = TypedDict("CustomerLogoutResult", {
    "signedOut": bool,
    "sessions": float,
})

CustomerLogoutEverywhereResult = TypedDict("CustomerLogoutEverywhereResult", {
    "signedOut": bool,
    "sessions": float,
})

WebhookEventName = Literal[
    "order.created",
    "order.payment_started",
    "order.paid",
    "order.delivered",
    "order.redelivered",
    "order.email_failed",
    "order.cancelled",
    "order.refunded",
    "order.disputed",
    "order.chargeback",
    "order.payment_submitted",
    "order.rerouted",
    "review.created",
    "review.removed",
    "review.flag_declined",
    "stock.low",
    "stock.out",
    "product.created",
    "product.updated",
    "product.deleted",
    "customer.created",
    "customer.balance_changed",
    "affiliate.created",
    "affiliate.payout_requested",
    "affiliate.payout_answered",
    "affiliate.balance_changed",
    "subscription.started",
    "subscription.renewed",
    "subscription.cancelled",
    "subscription.ended",
    "subscription.paused",
    "subscription.resumed",
    "subscription.charge_failed",
    "cart.email_sent",
    "cart.recovered",
    "cart.unsubscribed",
    "routing.processor_paused",
    "routing.processor_resumed",
    "dispute.opened",
    "dispute.updated",
    "dispute.won",
    "dispute.lost",
    "dispute.closed",
    "fraud.checkout_blocked",
    "webhook.test",
]

WebhookEvent = TypedDict("WebhookEvent", {
    "id": str,
    "event": WebhookEventName,
    "createdAt": str,
    "storeId": str,
    "data": Dict[str, Any],
})
