# Written by scripts/generate.py from the API reference. Do not edit by hand.

import os
from typing import Any, BinaryIO, Dict, List, Literal, Optional, Union, cast

from .._files import File
from .._page import Page
from .types import (
    AffiliateProgrammeShowResult,
    AffiliateProgrammeUpdateResult,
    AffiliatesCreateResult,
    AffiliatesDeleteResultItem,
    AffiliatesHistoryResult,
    AffiliatesHistoryResultChangesItem,
    AffiliatesListResultItem,
    AffiliatesSetBalanceResult,
    AffiliatesUpdateResult,
    AnalyticsLiveResult,
    AnalyticsLiveResultHome,
    AnalyticsLiveResultNow,
    AnalyticsLiveResultToday,
    AnalyticsOverviewResult,
    AnalyticsOverviewResultChange,
    AnalyticsOverviewResultCustomerSeries,
    AnalyticsOverviewResultCustomerSeriesPointsItem,
    AnalyticsOverviewResultFunnelItem,
    AnalyticsOverviewResultLifetime,
    AnalyticsOverviewResultPrevious,
    AnalyticsOverviewResultRange,
    AnalyticsOverviewResultReturningCustomers,
    AnalyticsOverviewResultReturningCustomersPrevious,
    AnalyticsOverviewResultSeries,
    AnalyticsOverviewResultSeriesPointsItem,
    AnalyticsOverviewResultStatusCounts,
    AnalyticsOverviewResultStatusTotals,
    AnalyticsOverviewResultStatusTotalsCancelled,
    AnalyticsOverviewResultStatusTotalsChargeback,
    AnalyticsOverviewResultStatusTotalsCompleted,
    AnalyticsOverviewResultStatusTotalsImported,
    AnalyticsOverviewResultStatusTotalsPending,
    AnalyticsOverviewResultStatusTotalsRefunded,
    AnalyticsOverviewResultStore,
    AnalyticsOverviewResultTopCountriesItem,
    AnalyticsOverviewResultTopPaymentMethodsItem,
    AnalyticsOverviewResultTopProductsItem,
    AnalyticsOverviewResultTotals,
    AnalyticsOverviewResultTotalsRecovered,
    AnalyticsReportResult,
    AnalyticsReportResultBrowsers,
    AnalyticsReportResultCampaigns,
    AnalyticsReportResultChange,
    AnalyticsReportResultChannels,
    AnalyticsReportResultCities,
    AnalyticsReportResultCountries,
    AnalyticsReportResultDevices,
    AnalyticsReportResultEngines,
    AnalyticsReportResultExit,
    AnalyticsReportResultLanding,
    AnalyticsReportResultPages,
    AnalyticsReportResultPrevious,
    AnalyticsReportResultRange,
    AnalyticsReportResultReferrers,
    AnalyticsReportResultSeries,
    AnalyticsReportResultSeriesPointsItem,
    AnalyticsReportResultSources,
    AnalyticsReportResultStore,
    AnalyticsReportResultSystems,
    AnalyticsReportResultTotals,
    AnalyticsVisitorsNowResult,
    BlacklistCreateResult,
    BlacklistDeleteResult,
    BlacklistListItem,
    BlacklistSetEnabledResult,
    BlacklistUpdateResult,
    BlogCategoriesCreateResult,
    BlogCategoriesDeleteResult,
    BlogCategoriesSortResult,
    BlogCategoriesUpdateResult,
    BlogListResultItem,
    BlogListResultItemPostsItem,
    BlogPostsCreateResult,
    BlogPostsCreateResultSearch,
    BlogPostsCreateResultSearchChecksItem,
    BlogPostsDeleteResult,
    BlogPostsSetStatusResult,
    BlogPostsShowResult,
    BlogPostsShowResultSearch,
    BlogPostsShowResultSearchChecksItem,
    BlogPostsSortResult,
    BlogPostsUpdateResult,
    BlogPostsUpdateResultSearch,
    BlogPostsUpdateResultSearchChecksItem,
    CartRecoveryCartResult,
    CartRecoveryCartsItem,
    CartRecoveryShowResult,
    CartRecoveryUpdateResult,
    CategoriesCreateResult,
    CategoriesDeleteResult,
    CategoriesListResultItem,
    CategoriesSortResult,
    CategoriesUpdateResult,
    CouponCategoriesCreateResult,
    CouponCategoriesDeleteResult,
    CouponCategoriesListResultItem,
    CouponCategoriesUpdateResult,
    CouponPopupShowResult,
    CouponPopupUpdateResult,
    CouponPopupUpdateResultCoupon,
    CouponsCreateResult,
    CouponsDeleteResult,
    CouponsListItem,
    CouponsSortResult,
    CouponsUpdateResult,
    CustomMethodsCreateResult,
    CustomMethodsDeleteResultItem,
    CustomMethodsListResultItem,
    CustomMethodsSetEnabledResultItem,
    CustomMethodsSortResultItem,
    CustomMethodsUpdateResultItem,
    CustomerAffiliateJoinResult,
    CustomerAffiliateJoinResultBalance,
    CustomerAffiliateJoinResultCan,
    CustomerAffiliateJoinResultEarned,
    CustomerAffiliateJoinResultLimits,
    CustomerAffiliateJoinResultOffered,
    CustomerAffiliateJoinResultPaidOut,
    CustomerAffiliateLinkResult,
    CustomerAffiliateLinkResultBalance,
    CustomerAffiliateLinkResultCan,
    CustomerAffiliateLinkResultChangesItem,
    CustomerAffiliateLinkResultEarned,
    CustomerAffiliateLinkResultLimits,
    CustomerAffiliateLinkResultOffered,
    CustomerAffiliateLinkResultPaidOut,
    CustomerAffiliatePayoutsCancelResult,
    CustomerAffiliatePayoutsCancelResultBalance,
    CustomerAffiliatePayoutsCancelResultCan,
    CustomerAffiliatePayoutsCancelResultChangesItem,
    CustomerAffiliatePayoutsCancelResultEarned,
    CustomerAffiliatePayoutsCancelResultLimits,
    CustomerAffiliatePayoutsCancelResultOffered,
    CustomerAffiliatePayoutsCancelResultPaidOut,
    CustomerAffiliatePayoutsCancelResultPayoutsItem,
    CustomerAffiliatePayoutsCreateResult,
    CustomerAffiliatePayoutsCreateResultBalance,
    CustomerAffiliatePayoutsCreateResultCan,
    CustomerAffiliatePayoutsCreateResultChangesItem,
    CustomerAffiliatePayoutsCreateResultEarned,
    CustomerAffiliatePayoutsCreateResultLimits,
    CustomerAffiliatePayoutsCreateResultOffered,
    CustomerAffiliatePayoutsCreateResultPaidOut,
    CustomerAffiliatePayoutsCreateResultPayout,
    CustomerAffiliatePayoutsCreateResultPayoutsItem,
    CustomerAffiliateShowResult,
    CustomerAffiliateShowResultBalance,
    CustomerAffiliateShowResultCan,
    CustomerAffiliateShowResultChangesItem,
    CustomerAffiliateShowResultEarned,
    CustomerAffiliateShowResultLimits,
    CustomerAffiliateShowResultOffered,
    CustomerAffiliateShowResultPaidOut,
    CustomerAffiliateToStoreResult,
    CustomerAffiliateToStoreResultBalance,
    CustomerAffiliateToStoreResultCan,
    CustomerAffiliateToStoreResultChangesItem,
    CustomerAffiliateToStoreResultEarned,
    CustomerAffiliateToStoreResultLimits,
    CustomerAffiliateToStoreResultOffered,
    CustomerAffiliateToStoreResultPaidOut,
    CustomerAffiliateToStoreResultPayoutsItem,
    CustomerLoginResult,
    CustomerLogoutEverywhereResult,
    CustomerLogoutResult,
    CustomerOrdersShowResult,
    CustomerOrdersShowResultLinesItem,
    CustomerOrdersShowResultLinesItemDelivery,
    CustomerShowResult,
    CustomerShowResultAffiliate,
    CustomerShowResultDownloads,
    CustomerShowResultDownloadsInstructionsItem,
    CustomerShowResultDownloadsOrdersItem,
    CustomerShowResultDownloadsOrdersItemInstructionsItem,
    CustomerShowResultOrdersItem,
    CustomerShowResultTotals,
    CustomerShowResultTotalsSpentItem,
    CustomerSubscriptionsCancelResultItem,
    CustomerSubscriptionsListResultItem,
    CustomerSubscriptionsPauseResultItem,
    CustomerSubscriptionsResumeResultItem,
    CustomerSubscriptionsUndoResultItem,
    CustomerTagsAutomaticResultItem,
    CustomerTagsCreateResult,
    CustomerTagsListResultItem,
    CustomerTagsUpdateResult,
    CustomerTicketsCreateResult,
    CustomerTicketsCreateResultConversationItem,
    CustomerTicketsCreateResultLimits,
    CustomerTicketsListResultItem,
    CustomerTicketsReplyResult,
    CustomerTicketsReplyResultConversationItem,
    CustomerTicketsReplyResultLimits,
    CustomerTicketsResolveResult,
    CustomerTicketsResolveResultConversationItem,
    CustomerTicketsResolveResultLimits,
    CustomerTicketsShowResult,
    CustomerTicketsShowResultConversationItem,
    CustomerTicketsShowResultLimits,
    CustomerVerifyResult,
    CustomersBlacklistResult,
    CustomersBlacklistResultBalanceHistoryItem,
    CustomersBlacklistResultBlacklistedByItem,
    CustomersBlacklistResultTagsItem,
    CustomersCreateResult,
    CustomersListItem,
    CustomersListItemTagsItem,
    CustomersSetBalanceResult,
    CustomersSetBalanceResultBalanceHistoryItem,
    CustomersSetBalanceResultTagsItem,
    CustomersSetTagsResultItem,
    CustomersShowResult,
    CustomersShowResultBalanceHistoryItem,
    CustomersShowResultTagsItem,
    CustomersStatsResult,
    CustomersStatsResultAverageSpend,
    CustomersStatsResultCustomers,
    CustomersStatsResultNewCustomers,
    CustomersStatsResultRange,
    CustomersStatsResultReturning,
    CustomersTagResultItem,
    CustomersUnblacklistResult,
    CustomersUnblacklistResultBalanceHistoryItem,
    CustomersUnblacklistResultTagsItem,
    DisputesAccessResult,
    DisputesAccessResultAfterItem,
    DisputesAccessResultAnswer,
    DisputesAccessResultCan,
    DisputesAccessResultDraft,
    DisputesAccessResultHistoryItem,
    DisputesAccessResultOrder,
    DisputesAccessResultRecordsItem,
    DisputesAccessResultRecordsItemFactsItem,
    DisputesBlacklistResult,
    DisputesBlacklistResultAfterItem,
    DisputesBlacklistResultAnswer,
    DisputesBlacklistResultCan,
    DisputesBlacklistResultDraft,
    DisputesBlacklistResultHistoryItem,
    DisputesBlacklistResultOrder,
    DisputesBlacklistResultRecordsItem,
    DisputesBlacklistResultRecordsItemFactsItem,
    DisputesForOrderResultItem,
    DisputesForOrderResultItemAnswer,
    DisputesGetResult,
    DisputesGetResultAfterItem,
    DisputesGetResultAnswer,
    DisputesGetResultCan,
    DisputesGetResultDraft,
    DisputesGetResultHistoryItem,
    DisputesGetResultOrder,
    DisputesGetResultRecordsItem,
    DisputesGetResultRecordsItemFactsItem,
    DisputesListItem,
    DisputesListItemAnswer,
    DisputesMarkSubmittedResult,
    DisputesMarkSubmittedResultAfterItem,
    DisputesMarkSubmittedResultAnswer,
    DisputesMarkSubmittedResultCan,
    DisputesMarkSubmittedResultDraft,
    DisputesMarkSubmittedResultHistoryItem,
    DisputesMarkSubmittedResultOrder,
    DisputesMarkSubmittedResultRecordsItem,
    DisputesMarkSubmittedResultRecordsItemFactsItem,
    DisputesSaveDraftResult,
    DisputesSaveDraftResultAfterItem,
    DisputesSaveDraftResultAnswer,
    DisputesSaveDraftResultCan,
    DisputesSaveDraftResultDraft,
    DisputesSaveDraftResultHistoryItem,
    DisputesSaveDraftResultOrder,
    DisputesSaveDraftResultRecordsItem,
    DisputesSaveDraftResultRecordsItemFactsItem,
    DisputesSettingsResult,
    DisputesUpdateSettingsResult,
    DomainShowResult,
    EmailTemplatesListResultItem,
    EmailTemplatesPreviewResult,
    EmailTemplatesPreviewResultParts,
    EmailTemplatesPreviewResultProblems,
    EmailTemplatesPreviewResultValues,
    EmailTemplatesRevertResult,
    EmailTemplatesRevertResultPartsItem,
    EmailTemplatesRevertResultVariablesItem,
    EmailTemplatesSaveSharedResult,
    EmailTemplatesSharedResult,
    EmailTemplatesShowResult,
    EmailTemplatesShowResultPartsItem,
    EmailTemplatesShowResultVariablesItem,
    EmailTemplatesUpdateResult,
    EmailTemplatesUpdateResultPartsItem,
    EmailTemplatesUpdateResultVariablesItem,
    ExpenseCategoriesCreateResult,
    ExpenseCategoriesDeleteResult,
    ExpenseCategoriesListResultItem,
    ExpenseCategoriesSortResult,
    ExpenseCategoriesUpdateResult,
    ExpenseRulesCreateResult,
    ExpenseRulesCreateResultCategory,
    ExpenseRulesDeleteResult,
    ExpenseRulesListResultItem,
    ExpenseRulesListResultItemCategory,
    ExpensesCreateResult,
    ExpensesCreateResultCategory,
    ExpensesDeleteResult,
    ExpensesListResultItem,
    ExpensesListResultItemCategory,
    ExpensesSetupResult,
    ExpensesSetupResultCategoriesItem,
    ExpensesSetupResultLimits,
    ExpensesSetupResultMethodsItem,
    ExpensesSetupResultPayeesItem,
    ExpensesSetupResultReceipts,
    ExpensesSummaryResult,
    ExpensesSummaryResultCounts,
    ExpensesSummaryResultLargest,
    ExpensesSummaryResultMonthsItem,
    ExpensesSummaryResultPeriod,
    ExpensesSummaryResultReceipts,
    ExpensesSummaryResultRecurring,
    ExpensesUpdateResult,
    ExpensesUpdateResultCategory,
    FinanceAccessResult,
    FinanceAccountingResult,
    FinanceAccountingResultChecksItem,
    FinanceAccountingResultCountriesItem,
    FinanceAccountingResultCounts,
    FinanceAccountingResultLinesItem,
    FinanceAccountingResultMethodsItem,
    FinanceAccountingResultNow,
    FinanceAccountingResultPeriod,
    FinanceAccountingResultPrevious,
    FinanceAccountingResultTax,
    FinanceAccountingResultTaxReport,
    FinancePaymentCostsResult,
    FinancePaymentCostsResultLimits,
    FinancePaymentCostsResultRatesItem,
    FinanceProfitResult,
    FinanceProfitResultBreakEven,
    FinanceProfitResultFees,
    FinanceProfitResultMonthsItem,
    FinanceProfitResultNow,
    FinanceProfitResultPeriod,
    FinanceProfitResultPrevious,
    FinanceProfitResultProductsItem,
    FinanceProfitResultProductsItemVariantsItem,
    FinanceSetCostResult,
    FinanceSetPaymentCostsResultItem,
    FraudEventsListItem,
    FraudEventsListItemBy,
    FraudSettingsShowResult,
    FraudSettingsUpdateResult,
    InvoicesLinkResult,
    InvoicesListItem,
    KeyShowResult,
    KeyShowResultKey,
    KeyShowResultStore,
    OrdersApprovePaymentResult,
    OrdersListItem,
    OrdersListItemBilling,
    OrdersListItemItemsItem,
    OrdersMarkPaidResult,
    OrdersRedeliverResult,
    OrdersRedeliverResultEmail,
    OrdersRedeliverResultItemsItem,
    OrdersRefundResult,
    OrdersRejectPaymentResult,
    OrdersSetNoteResult,
    OrdersShowResult,
    OrdersShowResultBilling,
    OrdersShowResultCustomer,
    OrdersShowResultCustomerOrdersItem,
    OrdersShowResultCustomerTotals,
    OrdersShowResultItemsItem,
    OrdersShowResultRefund,
    OrdersShowResultRefundBalance,
    OrdersShowResultRefundRecord,
    OrdersShowResultRefundSource,
    OrdersShowResultTimelineItem,
    OrdersShowResultTimelineItemBy,
    PaymentMethodsListResultItem,
    PaymentMethodsListResultItemFieldsItem,
    PaymentMethodsListResultItemTogglesItem,
    PaymentMethodsSetBalanceResultItem,
    PaymentMethodsSetBalanceResultItemFieldsItem,
    PaymentMethodsSetBalanceResultItemTogglesItem,
    PaymentMethodsSetMethodUnpaidHoursResultItem,
    PaymentMethodsSetMethodUnpaidHoursResultItemFieldsItem,
    PaymentMethodsSetMethodUnpaidHoursResultItemTogglesItem,
    PaymentMethodsSetUnpaidHoursResultItem,
    PaymentMethodsSetUnpaidHoursResultItemFieldsItem,
    PaymentMethodsSetUnpaidHoursResultItemTogglesItem,
    ProductsBulkUpdateResult,
    ProductsCreateResult,
    ProductsCreateResultBadgesItem,
    ProductsCreateResultFeaturesItem,
    ProductsCreateResultVariantsItem,
    ProductsListItem,
    ProductsListItemBadgesItem,
    ProductsListItemFeaturesItem,
    ProductsListItemVariantsItem,
    ProductsSetVisibilityResult,
    ProductsShowResult,
    ProductsShowResultBadgesItem,
    ProductsShowResultFeaturesItem,
    ProductsShowResultVariantsItem,
    ProductsSortResult,
    ProductsUpdateResult,
    ProductsUpdateResultBadgesItem,
    ProductsUpdateResultFeaturesItem,
    ProductsUpdateResultVariantsItem,
    RecurringExpensesCreateResult,
    RecurringExpensesDeleteResult,
    RecurringExpensesListResultItem,
    RecurringExpensesSkipResult,
    RecurringExpensesSkipResultRecurring,
    RecurringExpensesUpdateResult,
    RedirectsCreateResultItem,
    RedirectsListResultItem,
    RedirectsUpdateResultItem,
    RequestsListItem,
    RequestsListItemApiKey,
    RequestsShowResult,
    RequestsShowResultApiKey,
    ReviewsListItem,
    ReviewsListItemFlag,
    ReviewsListItemItemsItem,
    RoutingAddProcessorResult,
    RoutingAddProcessorResultAvailableItem,
    RoutingAddProcessorResultFigures,
    RoutingAddProcessorResultFiguresRouted,
    RoutingAddProcessorResultFiguresSaved,
    RoutingAddProcessorResultLimits,
    RoutingAddProcessorResultProcessorsItem,
    RoutingAddProcessorResultSettings,
    RoutingAddRuleResult,
    RoutingAddRuleResultFigures,
    RoutingAddRuleResultFiguresRouted,
    RoutingAddRuleResultFiguresSaved,
    RoutingAddRuleResultLimits,
    RoutingAddRuleResultProcessorsItem,
    RoutingAddRuleResultRulesItem,
    RoutingAddRuleResultSettings,
    RoutingDeleteRuleResult,
    RoutingDeleteRuleResultFigures,
    RoutingDeleteRuleResultFiguresRouted,
    RoutingDeleteRuleResultFiguresSaved,
    RoutingDeleteRuleResultLimits,
    RoutingDeleteRuleResultProcessorsItem,
    RoutingDeleteRuleResultSettings,
    RoutingRemoveProcessorResult,
    RoutingRemoveProcessorResultAvailableItem,
    RoutingRemoveProcessorResultFigures,
    RoutingRemoveProcessorResultFiguresRouted,
    RoutingRemoveProcessorResultFiguresSaved,
    RoutingRemoveProcessorResultLimits,
    RoutingRemoveProcessorResultProcessorsItem,
    RoutingRemoveProcessorResultSettings,
    RoutingResumeProcessorResult,
    RoutingResumeProcessorResultFigures,
    RoutingResumeProcessorResultFiguresRouted,
    RoutingResumeProcessorResultFiguresSaved,
    RoutingResumeProcessorResultLimits,
    RoutingResumeProcessorResultProcessorsItem,
    RoutingResumeProcessorResultRulesItem,
    RoutingResumeProcessorResultSettings,
    RoutingShowResult,
    RoutingShowResultFigures,
    RoutingShowResultFiguresRouted,
    RoutingShowResultFiguresSaved,
    RoutingShowResultLimits,
    RoutingShowResultProcessorsItem,
    RoutingShowResultRulesItem,
    RoutingShowResultSettings,
    RoutingSortProcessorsResult,
    RoutingSortProcessorsResultFigures,
    RoutingSortProcessorsResultFiguresRouted,
    RoutingSortProcessorsResultFiguresSaved,
    RoutingSortProcessorsResultLimits,
    RoutingSortProcessorsResultProcessorsItem,
    RoutingSortProcessorsResultSettings,
    RoutingSortRulesResult,
    RoutingSortRulesResultFigures,
    RoutingSortRulesResultFiguresRouted,
    RoutingSortRulesResultFiguresSaved,
    RoutingSortRulesResultLimits,
    RoutingSortRulesResultProcessorsItem,
    RoutingSortRulesResultRulesItem,
    RoutingSortRulesResultSettings,
    RoutingUpdateProcessorResult,
    RoutingUpdateProcessorResultFigures,
    RoutingUpdateProcessorResultFiguresRouted,
    RoutingUpdateProcessorResultFiguresSaved,
    RoutingUpdateProcessorResultLimits,
    RoutingUpdateProcessorResultProcessorsItem,
    RoutingUpdateProcessorResultSettings,
    RoutingUpdateResult,
    RoutingUpdateResultFigures,
    RoutingUpdateResultFiguresRouted,
    RoutingUpdateResultFiguresSaved,
    RoutingUpdateResultLimits,
    RoutingUpdateResultProcessorsItem,
    RoutingUpdateResultRulesItem,
    RoutingUpdateResultSettings,
    RoutingUpdateRuleResult,
    RoutingUpdateRuleResultFigures,
    RoutingUpdateRuleResultFiguresRouted,
    RoutingUpdateRuleResultFiguresSaved,
    RoutingUpdateRuleResultLimits,
    RoutingUpdateRuleResultProcessorsItem,
    RoutingUpdateRuleResultRulesItem,
    RoutingUpdateRuleResultSettings,
    SalesCreateResult,
    SalesDeleteResult,
    SalesListResultItem,
    SalesSetEnabledResult,
    SalesShowResult,
    SeoShowResult,
    SeoShowResultAnalytics,
    SeoUpdateResult,
    SeoUpdateResultAnalytics,
    SitemapShowResult,
    SitemapShowResultKindsItem,
    SitemapShowResultKindsItemEntriesItem,
    SitemapUpdateKindResult,
    SitemapUpdateKindResultKindsItem,
    SitemapUpdateKindResultKindsItemEntriesItem,
    StockAddKeysResult,
    StockDeleteKeysResult,
    StockListKeysItem,
    StoreEmailSettingsResult,
    StoreEmailSettingsResultTestEmailEvery,
    StoreShowResult,
    StoreShowResultCurrenciesItem,
    StoreShowResultSocialLinks,
    StoreUpdateResult,
    StoreUpdateResultCurrenciesItem,
    StoreUpdateResultSocialLinks,
    StorefrontsCodeAddResult,
    StorefrontsCodeAddResultCode,
    StorefrontsCodeAddResultCodeFilesItem,
    StorefrontsCodeAddResultCodeFolders,
    StorefrontsCodeAddResultCodeLimits,
    StorefrontsCodeAddResultFile,
    StorefrontsCodeDeleteResult,
    StorefrontsCodeFileResult,
    StorefrontsCodePublishResult,
    StorefrontsCodePublishResultCode,
    StorefrontsCodePublishResultCodeFilesItem,
    StorefrontsCodePublishResultCodeFolders,
    StorefrontsCodePublishResultCodeLimits,
    StorefrontsCodePublishResultPreview,
    StorefrontsCodePublishResultPreviewPagesItem,
    StorefrontsCodePublishResultStorefront,
    StorefrontsCodePublishResultVersionsItem,
    StorefrontsCodeRenameResult,
    StorefrontsCodeRenameResultFile,
    StorefrontsCodeResult,
    StorefrontsCodeResultStorefront,
    StorefrontsCodeSaveResult,
    StorefrontsCodeSaveResultCode,
    StorefrontsCodeSaveResultCodeFilesItem,
    StorefrontsCodeSaveResultCodeFolders,
    StorefrontsCodeSaveResultCodeLimits,
    StorefrontsCodeSaveResultFile,
    StorefrontsCodeStartResult,
    StorefrontsCodeStartResultCode,
    StorefrontsCodeStartResultCodeFilesItem,
    StorefrontsCodeStartResultCodeFolders,
    StorefrontsCodeStartResultCodeLimits,
    StorefrontsCodeStartResultPreview,
    StorefrontsCodeStartResultPreviewPagesItem,
    StorefrontsCodeStartResultStorefront,
    StorefrontsCreateResultItem,
    StorefrontsDeleteResultItem,
    StorefrontsExportResult,
    StorefrontsExportResultStorefront,
    StorefrontsExportResultStorefrontDesign,
    StorefrontsExportResultStorefrontDesignAnnouncement,
    StorefrontsExportResultStorefrontDesignCart,
    StorefrontsExportResultStorefrontDesignFooter,
    StorefrontsExportResultStorefrontDesignFooterColumnsItem,
    StorefrontsExportResultStorefrontDesignHeader,
    StorefrontsExportResultStorefrontDesignHeaderNavItem,
    StorefrontsExportResultStorefrontDesignPagesItem,
    StorefrontsExportResultStorefrontDesignTheme,
    StorefrontsListResultItem,
    StorefrontsRenameResultItem,
    StorefrontsSetLiveResultItem,
    SubscribersAskingResult,
    SubscribersListItem,
    SubscribersSummaryResult,
    SubscribersSummaryResultFigures,
    SubscribersUnsubscribeResult,
    SubscriptionsAddDaysResult,
    SubscriptionsCancelResult,
    SubscriptionsEmailResult,
    SubscriptionsListItem,
    SubscriptionsPauseResult,
    SubscriptionsPlansResultItem,
    SubscriptionsResumeResult,
    SubscriptionsSavePlansResultItem,
    SubscriptionsSettingsResult,
    SubscriptionsShowResult,
    SubscriptionsUndoResult,
    SubscriptionsUpdateSettingsResult,
    TaxDeleteRateResult,
    TaxDeleteRateResultRatesItem,
    TaxDeleteRateResultRegions,
    TaxDeleteRateResultRegionsUSItem,
    TaxDeleteRateResultStandard,
    TaxDeleteRateResultStandardAE,
    TaxDeleteRateResultStandardAR,
    TaxDeleteRateResultStandardAT,
    TaxDeleteRateResultStandardAU,
    TaxDeleteRateResultStandardBE,
    TaxDeleteRateResultStandardBG,
    TaxDeleteRateResultStandardBH,
    TaxDeleteRateResultStandardCA,
    TaxDeleteRateResultStandardCH,
    TaxDeleteRateResultStandardCL,
    TaxDeleteRateResultStandardCO,
    TaxDeleteRateResultStandardCY,
    TaxDeleteRateResultStandardCZ,
    TaxDeleteRateResultStandardDE,
    TaxDeleteRateResultStandardDK,
    TaxDeleteRateResultStandardEE,
    TaxDeleteRateResultStandardEG,
    TaxDeleteRateResultStandardES,
    TaxDeleteRateResultStandardFI,
    TaxDeleteRateResultStandardFR,
    TaxDeleteRateResultStandardGB,
    TaxDeleteRateResultStandardGR,
    TaxDeleteRateResultStandardHR,
    TaxDeleteRateResultStandardHU,
    TaxDeleteRateResultStandardID,
    TaxDeleteRateResultStandardIE,
    TaxDeleteRateResultStandardIL,
    TaxDeleteRateResultStandardIN,
    TaxDeleteRateResultStandardIS,
    TaxDeleteRateResultStandardIT,
    TaxDeleteRateResultStandardJP,
    TaxDeleteRateResultStandardKE,
    TaxDeleteRateResultStandardKR,
    TaxDeleteRateResultStandardLI,
    TaxDeleteRateResultStandardLT,
    TaxDeleteRateResultStandardLU,
    TaxDeleteRateResultStandardLV,
    TaxDeleteRateResultStandardMA,
    TaxDeleteRateResultStandardMT,
    TaxDeleteRateResultStandardMX,
    TaxDeleteRateResultStandardMY,
    TaxDeleteRateResultStandardNG,
    TaxDeleteRateResultStandardNL,
    TaxDeleteRateResultStandardNO,
    TaxDeleteRateResultStandardNZ,
    TaxDeleteRateResultStandardOM,
    TaxDeleteRateResultStandardPE,
    TaxDeleteRateResultStandardPH,
    TaxDeleteRateResultStandardPL,
    TaxDeleteRateResultStandardPT,
    TaxDeleteRateResultStandardRO,
    TaxDeleteRateResultStandardRS,
    TaxDeleteRateResultStandardSA,
    TaxDeleteRateResultStandardSE,
    TaxDeleteRateResultStandardSG,
    TaxDeleteRateResultStandardSI,
    TaxDeleteRateResultStandardSK,
    TaxDeleteRateResultStandardTH,
    TaxDeleteRateResultStandardTR,
    TaxDeleteRateResultStandardTW,
    TaxDeleteRateResultStandardUA,
    TaxDeleteRateResultStandardVN,
    TaxDeleteRateResultStandardZA,
    TaxSetRatesResult,
    TaxSetRatesResultRatesItem,
    TaxSetRatesResultRegions,
    TaxSetRatesResultRegionsUSItem,
    TaxSetRatesResultStandard,
    TaxSetRatesResultStandardAE,
    TaxSetRatesResultStandardAR,
    TaxSetRatesResultStandardAT,
    TaxSetRatesResultStandardAU,
    TaxSetRatesResultStandardBE,
    TaxSetRatesResultStandardBG,
    TaxSetRatesResultStandardBH,
    TaxSetRatesResultStandardCA,
    TaxSetRatesResultStandardCH,
    TaxSetRatesResultStandardCL,
    TaxSetRatesResultStandardCO,
    TaxSetRatesResultStandardCY,
    TaxSetRatesResultStandardCZ,
    TaxSetRatesResultStandardDE,
    TaxSetRatesResultStandardDK,
    TaxSetRatesResultStandardEE,
    TaxSetRatesResultStandardEG,
    TaxSetRatesResultStandardES,
    TaxSetRatesResultStandardFI,
    TaxSetRatesResultStandardFR,
    TaxSetRatesResultStandardGB,
    TaxSetRatesResultStandardGR,
    TaxSetRatesResultStandardHR,
    TaxSetRatesResultStandardHU,
    TaxSetRatesResultStandardID,
    TaxSetRatesResultStandardIE,
    TaxSetRatesResultStandardIL,
    TaxSetRatesResultStandardIN,
    TaxSetRatesResultStandardIS,
    TaxSetRatesResultStandardIT,
    TaxSetRatesResultStandardJP,
    TaxSetRatesResultStandardKE,
    TaxSetRatesResultStandardKR,
    TaxSetRatesResultStandardLI,
    TaxSetRatesResultStandardLT,
    TaxSetRatesResultStandardLU,
    TaxSetRatesResultStandardLV,
    TaxSetRatesResultStandardMA,
    TaxSetRatesResultStandardMT,
    TaxSetRatesResultStandardMX,
    TaxSetRatesResultStandardMY,
    TaxSetRatesResultStandardNG,
    TaxSetRatesResultStandardNL,
    TaxSetRatesResultStandardNO,
    TaxSetRatesResultStandardNZ,
    TaxSetRatesResultStandardOM,
    TaxSetRatesResultStandardPE,
    TaxSetRatesResultStandardPH,
    TaxSetRatesResultStandardPL,
    TaxSetRatesResultStandardPT,
    TaxSetRatesResultStandardRO,
    TaxSetRatesResultStandardRS,
    TaxSetRatesResultStandardSA,
    TaxSetRatesResultStandardSE,
    TaxSetRatesResultStandardSG,
    TaxSetRatesResultStandardSI,
    TaxSetRatesResultStandardSK,
    TaxSetRatesResultStandardTH,
    TaxSetRatesResultStandardTR,
    TaxSetRatesResultStandardTW,
    TaxSetRatesResultStandardUA,
    TaxSetRatesResultStandardVN,
    TaxSetRatesResultStandardZA,
    TaxShowResult,
    TaxShowResultRatesItem,
    TaxShowResultRegions,
    TaxShowResultRegionsUSItem,
    TaxShowResultStandard,
    TaxShowResultStandardAE,
    TaxShowResultStandardAR,
    TaxShowResultStandardAT,
    TaxShowResultStandardAU,
    TaxShowResultStandardBE,
    TaxShowResultStandardBG,
    TaxShowResultStandardBH,
    TaxShowResultStandardCA,
    TaxShowResultStandardCH,
    TaxShowResultStandardCL,
    TaxShowResultStandardCO,
    TaxShowResultStandardCY,
    TaxShowResultStandardCZ,
    TaxShowResultStandardDE,
    TaxShowResultStandardDK,
    TaxShowResultStandardEE,
    TaxShowResultStandardEG,
    TaxShowResultStandardES,
    TaxShowResultStandardFI,
    TaxShowResultStandardFR,
    TaxShowResultStandardGB,
    TaxShowResultStandardGR,
    TaxShowResultStandardHR,
    TaxShowResultStandardHU,
    TaxShowResultStandardID,
    TaxShowResultStandardIE,
    TaxShowResultStandardIL,
    TaxShowResultStandardIN,
    TaxShowResultStandardIS,
    TaxShowResultStandardIT,
    TaxShowResultStandardJP,
    TaxShowResultStandardKE,
    TaxShowResultStandardKR,
    TaxShowResultStandardLI,
    TaxShowResultStandardLT,
    TaxShowResultStandardLU,
    TaxShowResultStandardLV,
    TaxShowResultStandardMA,
    TaxShowResultStandardMT,
    TaxShowResultStandardMX,
    TaxShowResultStandardMY,
    TaxShowResultStandardNG,
    TaxShowResultStandardNL,
    TaxShowResultStandardNO,
    TaxShowResultStandardNZ,
    TaxShowResultStandardOM,
    TaxShowResultStandardPE,
    TaxShowResultStandardPH,
    TaxShowResultStandardPL,
    TaxShowResultStandardPT,
    TaxShowResultStandardRO,
    TaxShowResultStandardRS,
    TaxShowResultStandardSA,
    TaxShowResultStandardSE,
    TaxShowResultStandardSG,
    TaxShowResultStandardSI,
    TaxShowResultStandardSK,
    TaxShowResultStandardTH,
    TaxShowResultStandardTR,
    TaxShowResultStandardTW,
    TaxShowResultStandardUA,
    TaxShowResultStandardVN,
    TaxShowResultStandardZA,
    TaxUpdateResult,
    TaxUpdateResultRegions,
    TaxUpdateResultRegionsUSItem,
    TaxUpdateResultStandard,
    TaxUpdateResultStandardAE,
    TaxUpdateResultStandardAR,
    TaxUpdateResultStandardAT,
    TaxUpdateResultStandardAU,
    TaxUpdateResultStandardBE,
    TaxUpdateResultStandardBG,
    TaxUpdateResultStandardBH,
    TaxUpdateResultStandardCA,
    TaxUpdateResultStandardCH,
    TaxUpdateResultStandardCL,
    TaxUpdateResultStandardCO,
    TaxUpdateResultStandardCY,
    TaxUpdateResultStandardCZ,
    TaxUpdateResultStandardDE,
    TaxUpdateResultStandardDK,
    TaxUpdateResultStandardEE,
    TaxUpdateResultStandardEG,
    TaxUpdateResultStandardES,
    TaxUpdateResultStandardFI,
    TaxUpdateResultStandardFR,
    TaxUpdateResultStandardGB,
    TaxUpdateResultStandardGR,
    TaxUpdateResultStandardHR,
    TaxUpdateResultStandardHU,
    TaxUpdateResultStandardID,
    TaxUpdateResultStandardIE,
    TaxUpdateResultStandardIL,
    TaxUpdateResultStandardIN,
    TaxUpdateResultStandardIS,
    TaxUpdateResultStandardIT,
    TaxUpdateResultStandardJP,
    TaxUpdateResultStandardKE,
    TaxUpdateResultStandardKR,
    TaxUpdateResultStandardLI,
    TaxUpdateResultStandardLT,
    TaxUpdateResultStandardLU,
    TaxUpdateResultStandardLV,
    TaxUpdateResultStandardMA,
    TaxUpdateResultStandardMT,
    TaxUpdateResultStandardMX,
    TaxUpdateResultStandardMY,
    TaxUpdateResultStandardNG,
    TaxUpdateResultStandardNL,
    TaxUpdateResultStandardNO,
    TaxUpdateResultStandardNZ,
    TaxUpdateResultStandardOM,
    TaxUpdateResultStandardPE,
    TaxUpdateResultStandardPH,
    TaxUpdateResultStandardPL,
    TaxUpdateResultStandardPT,
    TaxUpdateResultStandardRO,
    TaxUpdateResultStandardRS,
    TaxUpdateResultStandardSA,
    TaxUpdateResultStandardSE,
    TaxUpdateResultStandardSG,
    TaxUpdateResultStandardSI,
    TaxUpdateResultStandardSK,
    TaxUpdateResultStandardTH,
    TaxUpdateResultStandardTR,
    TaxUpdateResultStandardTW,
    TaxUpdateResultStandardUA,
    TaxUpdateResultStandardVN,
    TaxUpdateResultStandardZA,
    TeamActivityItem,
    TeamActivityItemSubject,
    TeamCancelInviteResult,
    TeamGetResult,
    TeamGetResultInvitesItem,
    TeamGetResultLimits,
    TeamGetResultMe,
    TeamGetResultOwner,
    TeamGetResultPermissions,
    TeamGetResultPermissionsGroupsItem,
    TeamGetResultPermissionsGroupsItemPermissionsItem,
    TeamGetResultPermissionsPresetsItem,
    TeamGetResultTeamsItem,
    TeamGetResultTeamsItemPeopleItem,
    TeamInviteResult,
    TeamInviteResultInvitesItem,
    TeamMoveMemberResult,
    TeamRemoveMemberResult,
    TeamResendInviteResult,
    TeamsCreateResult,
    TeamsDeleteResult,
    TeamsUpdateResult,
    TicketsGetResult,
    TicketsGetResultConversationItem,
    TicketsGetResultCustomer,
    TicketsGetResultLimits,
    TicketsGetResultOrder,
    TicketsGetResultOrdersItem,
    TicketsListItem,
    TicketsReopenResult,
    TicketsReopenResultConversationItem,
    TicketsReopenResultCustomer,
    TicketsReopenResultLimits,
    TicketsReopenResultOrder,
    TicketsReopenResultOrdersItem,
    TicketsReplyResult,
    TicketsReplyResultConversationItem,
    TicketsReplyResultCustomer,
    TicketsReplyResultLimits,
    TicketsReplyResultOrder,
    TicketsReplyResultOrdersItem,
    TicketsResolveResult,
    TicketsResolveResultConversationItem,
    TicketsResolveResultCustomer,
    TicketsResolveResultLimits,
    TicketsResolveResultOrder,
    TicketsResolveResultOrdersItem,
    TicketsSettingsResult,
    UpsellsCreateResult,
    UpsellsCreateResultTargetsItem,
    UpsellsDeleteResult,
    UpsellsListResultItem,
    UpsellsListResultItemTargetsItem,
    UpsellsSetEnabledResult,
    UpsellsSetEnabledResultTargetsItem,
    UpsellsSettingsResult,
    UpsellsSortResult,
    UpsellsUpdateResult,
    UpsellsUpdateResultTargetsItem,
    WebhooksCreateResult,
    WebhooksDeleteResult,
    WebhooksListResultItem,
    WebhooksShowResult,
    WebhooksUpdateResult,
    WinBackBuyerResult,
    WinBackBuyersItem,
    WinBackShowResult,
    WinBackUpdateResult,
)


class Key:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def show(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> KeyShowResult:
        """**Get the current key**

        What the key in the request is: its name, the permissions it carries, the addresses it accepts, and the store it belongs to with that store's ID. Make this your first call. Every other address needs the store's ID, and `api` in the answer is where that store's routes begin.

        An app's token is a key of the store it was approved for, and `app` says which app it is (null for the store's own keys): an app connected to many stores asks this to learn which store a token is for.

        Any live key may ask it, whatever its permissions.

        Any live API key may call this, whatever its permissions.

        Docs: https://docs.shoply.gg/api-reference/api-key/get-the-current-key
        """
        return cast("KeyShowResult", self._caller._call("key.show", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Store:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def show(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> StoreShowResult:
        """**Get the store**

        The store's details and settings: its name and address, currency, branding, links, policies, what its storefront shows, and its business details.

        Needs the `store.read` permission (Read Store).

        Docs: https://docs.shoply.gg/api-reference/store/get-the-store
        """
        return cast("StoreShowResult", self._caller._call("store.show", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        *,
        name: str,
        description: Optional[str] = None,
        currencyCode: Optional[str] = None,
        adaptivePricing: Optional[bool] = None,
        accentColor: Optional[str] = None,
        locale: Optional[str] = None,
        lowStockThreshold: Optional[int] = None,
        supportUrl: Optional[str] = None,
        guideUrl: Optional[str] = None,
        panelUrl: Optional[str] = None,
        socialLinks: Optional[Dict[str, Any]] = None,
        customLinks: Optional[List[Dict[str, Any]]] = None,
        termsOfService: Optional[str] = None,
        refundPolicy: Optional[str] = None,
        logoUrl: Optional[str] = None,
        faviconUrl: Optional[str] = None,
        storefrontPassword: Optional[str] = None,
        publishStock: Optional[bool] = None,
        autoReviews: Optional[bool] = None,
        publicStats: Optional[bool] = None,
        saleNotifications: Optional[bool] = None,
        publicOnline: Optional[bool] = None,
        active: Optional[bool] = None,
        businessType: Optional[Literal["sole_proprietorship", "partnership", "llc", "corporation", "nonprofit", "other"]] = None,
        businessName: Optional[str] = None,
        businessTaxId: Optional[str] = None,
        businessVatNumber: Optional[str] = None,
        businessLine1: Optional[str] = None,
        businessLine2: Optional[str] = None,
        businessCity: Optional[str] = None,
        businessRegion: Optional[str] = None,
        businessPostalCode: Optional[str] = None,
        businessCountry: Optional[str] = None,
        invoiceFooter: Optional[str] = None,
        expectedVersion: Optional[str] = None,
        expectedUpdatedAt: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> StoreUpdateResult:
        """**Update the store**

        Saves the store's settings. Read the store first and send it back changed: `name` is needed, and `description`, `logoUrl`, `supportUrl`, `guideUrl` and `panelUrl` are cleared when left out. Every other field stays as it is when left out.

        The store's address is changed with "Change the store's address", and its logo and icon are uploaded with their own routes.

        Needs the `store.write` permission (Change Store).

        Args:
            name: The store's name. Required.
            description: What the store says about itself.
            currencyCode: The currency its prices are in, as a three-letter code.
            adaptivePricing: Whether buyers are shown and charged prices in their own currency.
            accentColor: The store's colour, as `#rrggbb`.
            locale: The store's language and region, like `en-GB` or `de-DE`.
            lowStockThreshold: How few license keys a variant has left when the store is alerted.
            supportUrl: Where buyers get help.
            guideUrl: Where buyers find instructions.
            panelUrl: A panel of the store's own that buyers sign in to.
            socialLinks: The store's social networks: a network's name and its link. A blank link clears that network.
            customLinks: Links of the store's own, shown with its socials.
            termsOfService: The store's terms, as text.
            refundPolicy: The store's refund policy, as text.
            logoUrl: The store's logo, as "Get the store" answers it. Empty removes it.
            faviconUrl: The icon in the browser tab on the store's site. Empty removes it.
            storefrontPassword: A password visitors have to enter to see the storefront. Empty opens it to everybody.
            publishStock: Whether the storefront shows how many of a variant are left.
            autoReviews: Whether an order nobody reviewed is given five stars after seven days.
            publicStats: Whether the storefront shows items sold and customers.
            saleNotifications: Whether the storefront shows a note when somebody buys.
            publicOnline: Whether the storefront shows how many visitors are on it.
            active: Whether the store is open. Switched off, nothing can be bought.
            businessType: What kind of business it is.
            businessName: The business's name, printed on invoices. With `businessCountry`, it opens Finance.
            businessTaxId: Its tax number.
            businessVatNumber: Its VAT number.
            businessLine1: The first line of its address.
            businessLine2: The second.
            businessCity: Its city.
            businessRegion: Its state or region.
            businessPostalCode: Its postal code.
            businessCountry: Its country, as a two-letter code.
            invoiceFooter: A line printed at the foot of every invoice.
            expectedVersion: The `settingsVersion` you last read. Sent, the change is refused with `stale_write` only if something this route saves has changed since; the store's other settings (Support Tickets on or off, its tax, its payment options and the like) changing is not that. Use it rather than `expectedUpdatedAt`, which every one of them moves.
            expectedUpdatedAt: The `updatedAt` you last read. Sent, the change is refused with `stale_write` if the record has changed since. Left out, it is saved whatever happened in between.

        Docs: https://docs.shoply.gg/api-reference/store/update-the-store
        """
        return cast("StoreUpdateResult", self._caller._call("store.update", [], {"name": name, "description": description, "currencyCode": currencyCode, "adaptivePricing": adaptivePricing, "accentColor": accentColor, "locale": locale, "lowStockThreshold": lowStockThreshold, "supportUrl": supportUrl, "guideUrl": guideUrl, "panelUrl": panelUrl, "socialLinks": socialLinks, "customLinks": customLinks, "termsOfService": termsOfService, "refundPolicy": refundPolicy, "logoUrl": logoUrl, "faviconUrl": faviconUrl, "storefrontPassword": storefrontPassword, "publishStock": publishStock, "autoReviews": autoReviews, "publicStats": publicStats, "saleNotifications": saleNotifications, "publicOnline": publicOnline, "active": active, "businessType": businessType, "businessName": businessName, "businessTaxId": businessTaxId, "businessVatNumber": businessVatNumber, "businessLine1": businessLine1, "businessLine2": businessLine2, "businessCity": businessCity, "businessRegion": businessRegion, "businessPostalCode": businessPostalCode, "businessCountry": businessCountry, "invoiceFooter": invoiceFooter, "expectedVersion": expectedVersion, "expectedUpdatedAt": expectedUpdatedAt}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setAddress(
        self,
        *,
        slug: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Change the store's address**

        Moves the store to a new name under myshoply.gg. The old address leads to the new one. It can be changed once a week, and a name that is taken or reserved is refused.

        Needs the `store.write` permission (Change Store).

        Args:
            slug: The new name: the part before `.myshoply.gg`. Required.

        Docs: https://docs.shoply.gg/api-reference/store/change-the-stores-address
        """
        return cast("Any", self._caller._call("store.setAddress", [], {"slug": slug}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def uploadLogo(
        self,
        *,
        file: Union[str, "os.PathLike[str]", bytes, BinaryIO],
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Upload the store's logo**

        Gives the store its logo, replacing any it had. Sent as `multipart/form-data` in a field called `image`.

        Needs the `store.write` permission (Change Store).

        Args:
            file: A path on disk, the file's bytes, or a file opened for reading.
            filename: Its name. Left out, the path's own, or "upload".
            content_type: Its type, "image/png". Left out, worked out from the name.

        Docs: https://docs.shoply.gg/api-reference/store/upload-the-stores-logo
        """
        return cast("Any", self._caller._call("store.uploadLogo", [], {"file": file, "filename": filename, "content_type": content_type}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def uploadFavicon(
        self,
        *,
        file: Union[str, "os.PathLike[str]", bytes, BinaryIO],
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Upload the store's icon**

        Gives the store the icon its site shows in a browser tab, replacing any it had. Sent as `multipart/form-data` in a field called `image`.

        Needs the `store.write` permission (Change Store).

        Args:
            file: A path on disk, the file's bytes, or a file opened for reading.
            filename: Its name. Left out, the path's own, or "upload".
            content_type: Its type, "image/png". Left out, worked out from the name.

        Docs: https://docs.shoply.gg/api-reference/store/upload-the-stores-icon
        """
        return cast("Any", self._caller._call("store.uploadFavicon", [], {"file": file, "filename": filename, "content_type": content_type}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def emailSettings(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> StoreEmailSettingsResult:
        """**Get email and alert settings**

        What the store's emails say, which alerts it is sent, the coupon for a first order, and whether an order with no review is given one (`autoReviews`). Its Discord webhook is answered only as saved or not. These settings are changed in the dashboard.

        Needs the `store.read` permission (Read Store).

        Docs: https://docs.shoply.gg/api-reference/store/get-email-and-alert-settings
        """
        return cast("StoreEmailSettingsResult", self._caller._call("store.emailSettings", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Domain:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def show(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> DomainShowResult:
        """**Get the store's domain**

        The store's own domain, if it has connected one, with where it stands (`status`, and `checks`: whether it points here, whether its TXT record has proved it the store's, and whether its certificate is issued), and `cnameTarget`: what the domain's DNS record has to point at.

        Needs the `store.read` permission (Read Store).

        Docs: https://docs.shoply.gg/api-reference/domain/get-the-stores-domain
        """
        return cast("DomainShowResult", self._caller._call("domain.show", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def connect(
        self,
        *,
        hostname: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Connect a domain**

        Connects a domain of the store's own. Point a CNAME record for it at `cnameTarget` and it goes live once that is seen and its certificate is issued. A store has one domain: remove it to connect another.

        Needs the `store.write` permission (Change Store).

        Args:
            hostname: The domain, with no `https://` in front. Required.

        Docs: https://docs.shoply.gg/api-reference/domain/connect-a-domain
        """
        return cast("Any", self._caller._call("domain.connect", [], {"hostname": hostname}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def remove(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Remove the store's domain**

        Disconnects the store's own domain. The store goes on answering at its myshoply.gg address.

        Needs the `store.write` permission (Change Store).

        Docs: https://docs.shoply.gg/api-reference/domain/remove-the-stores-domain
        """
        return cast("Any", self._caller._call("domain.remove", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class PaymentMethods:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[PaymentMethodsListResultItem]:
        """**List payment methods**

        Every payment method Shoply supports, and for each whether this store has connected it and switched it on, in the order its checkout offers them. Never a method's credentials. `meta.balance` says whether buyers may pay with their store balance. A method's name here is the name the rest of the API uses for it. `meta.order` is every method the store has connected and every custom payment method it has (paid outside Shoply: "List custom payment methods"), by name or id, in the checkout's one order. Each method's `unpaidHours` is its own time for an unpaid order, or null for the store's, which is `meta.unpaid.hours`; `meta.routing.providers` is the card methods Payment Routing chooses between.

        Needs the `payments.read` permission (Read Payment Methods).

        Docs: https://docs.shoply.gg/api-reference/payment-methods/list-payment-methods
        """
        return cast("List[PaymentMethodsListResultItem]", self._caller._call("paymentMethods.list", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setEnabled(
        self,
        provider: str,
        *,
        enabled: bool,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Switch a payment method on or off**

        Takes a connected method off the checkout, or puts it back. Off keeps its credentials. On is refused for a method that is missing something it needs, which is put right in the dashboard. Answers the list again.

        Needs the `payments.write` permission (Change Payment Methods). Only a key the store's owner made, or an app the owner connected, can call it: one made by somebody on the store's team is refused (`owner_only`).

        Args:
            enabled: Whether the checkout offers it. Required.

        Docs: https://docs.shoply.gg/api-reference/payment-methods/switch-a-payment-method-on-or-off
        """
        return cast("Any", self._caller._call("paymentMethods.setEnabled", [provider], {"enabled": enabled}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def sort(
        self,
        *,
        providers: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Sort payment methods**

        Sets the order the checkout offers payment methods in. The first is the one most buyers take. Name some of them and they are put in this order in the places they hold now, and the rest stay where they are: a custom payment method between two connected ones stays between them. A custom method is named by its id in `meta.order`. Answers the list again.

        Needs the `payments.write` permission (Change Payment Methods). Only a key the store's owner made, or an app the owner connected, can call it: one made by somebody on the store's team is refused (`owner_only`).

        Args:
            providers: The methods' names in their new order. Required.

        Docs: https://docs.shoply.gg/api-reference/payment-methods/sort-payment-methods
        """
        return cast("Any", self._caller._call("paymentMethods.sort", [], {"providers": providers}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setBalance(
        self,
        *,
        enabled: bool,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[PaymentMethodsSetBalanceResultItem]:
        """**Switch paying with balance on or off**

        Whether the checkout offers buyers their balance at the store. Answers the list again.

        Needs the `payments.write` permission (Change Payment Methods). Only a key the store's owner made, or an app the owner connected, can call it: one made by somebody on the store's team is refused (`owner_only`).

        Args:
            enabled: Whether buyers may pay with their balance. Required.

        Docs: https://docs.shoply.gg/api-reference/payment-methods/switch-paying-with-balance-on-or-off
        """
        return cast("List[PaymentMethodsSetBalanceResultItem]", self._caller._call("paymentMethods.setBalance", [], {"enabled": enabled}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setUnpaidHours(
        self,
        *,
        hours: int,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[PaymentMethodsSetUnpaidHoursResultItem]:
        """**Set how long an unpaid order is kept**

        How long the store keeps an order nobody pays before it is cancelled, from 1 hour to 14 days. A method with a time of its own keeps its own. An order is never cancelled within an hour of a payment being opened on it. Answers the list again, with the store's time in `meta.unpaid`.

        Needs the `payments.write` permission (Change Payment Methods).

        Args:
            hours: Hours, from 1 to 336. Required.

        Docs: https://docs.shoply.gg/api-reference/payment-methods/set-how-long-an-unpaid-order-is-kept
        """
        return cast("List[PaymentMethodsSetUnpaidHoursResultItem]", self._caller._call("paymentMethods.setUnpaidHours", [], {"hours": hours}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setMethodUnpaidHours(
        self,
        provider: str,
        *,
        hours: int,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[PaymentMethodsSetMethodUnpaidHoursResultItem]:
        """**Set a payment method's own time for an unpaid order**

        How long an order is kept unpaid once a payment has been opened on it with this method, from 1 hour to 14 days. Null gives it back the store's time. Answers the list again, each method with its `unpaidHours`.

        Needs the `payments.write` permission (Change Payment Methods).

        Args:
            hours: Hours, from 1 to 336, or null for the store's. Required.

        Docs: https://docs.shoply.gg/api-reference/payment-methods/set-a-payment-methods-own-time-for-an-unpaid-order
        """
        return cast("List[PaymentMethodsSetMethodUnpaidHoursResultItem]", self._caller._call("paymentMethods.setMethodUnpaidHours", [provider], {"hours": hours}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Analytics:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def overview(
        self,
        *,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> AnalyticsOverviewResult:
        """**Get the overview**

        A period's headline figures (revenue, orders, customers and the rest), the same figures for the period before, and a day by day series. What the dashboard's home page draws.

        Needs the `analytics.read` permission (Read Analytics). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Args:
            range: The period. Left out, it is "30d".
            from_: The first day of a period of your own, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Its last day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.

        Docs: https://docs.shoply.gg/api-reference/analytics/get-the-overview
        """
        return cast("AnalyticsOverviewResult", self._caller._call("analytics.overview", [], {"range": range, "from": from_, "to": to, "tz": tz}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def report(
        self,
        *,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> AnalyticsReportResult:
        """**Get the visits report**

        A period's visits and what they went on to buy: visitors, where they came from by channel, website, campaign and affiliate, the pages they landed on, countries and devices. A sale is given to the last visit its buyer began before it, within 30 days. An order with no visit behind it (one made by hand, an invoice) counts in the totals and in none of the lists that say where sales came from.

        Needs the `analytics.read` permission (Read Analytics). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Args:
            range: The period. Left out, it is "30d".
            from_: The first day of a period of your own, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Its last day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.

        Docs: https://docs.shoply.gg/api-reference/analytics/get-the-visits-report
        """
        return cast("AnalyticsReportResult", self._caller._call("analytics.report", [], {"range": range, "from": from_, "to": to, "tz": tz}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def live(
        self,
        *,
        tz: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> AnalyticsLiveResult:
        """**Get the live view**

        What is happening on the store now: who is on it and where, the checkouts and orders of the last ten minutes, and the day's running totals.

        Needs the `analytics.read` permission (Read Analytics).

        Args:
            tz: The time zone "today" is in, as an IANA name. Left out, UTC.

        Docs: https://docs.shoply.gg/api-reference/analytics/get-the-live-view
        """
        return cast("AnalyticsLiveResult", self._caller._call("analytics.live", [], {"tz": tz}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def visitorsNow(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> AnalyticsVisitorsNowResult:
        """**Get visitors now**

        How many visitors are on the store now: one number, counted over the last ten minutes.

        Needs the `analytics.read` permission (Read Analytics).

        Docs: https://docs.shoply.gg/api-reference/analytics/get-visitors-now
        """
        return cast("AnalyticsVisitorsNowResult", self._caller._call("analytics.visitorsNow", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def search(
        self,
        *,
        provider: Optional[Literal["google", "bing"]] = None,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        dimension: Optional[Literal["query", "page", "country", "device"]] = None,
        value: Optional[str] = None,
        find: Optional[str] = None,
        findIn: Optional[Literal["query", "page"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Get the search report**

        How the store was found in a search engine over a period: clicks, impressions, click rate and position, over time and by search, page, country and device. From an engine the store has connected in the dashboard. With none connected it is refused with `search_unavailable`. Neither engine has figures for today.

        Needs the `analytics.read` permission (Read Analytics). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Args:
            provider: Which engine. Left out, it is "google".
            range: The period. Left out, it is "30d".
            from_: The first day of a period of your own, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Its last day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.
            dimension: To ask about one thing: what kind of thing `value` is.
            value: The one search, page, country or device to ask about.
            find: Only rows of one list that contain these words.
            findIn: Which list `find` narrows.

        Docs: https://docs.shoply.gg/api-reference/analytics/get-the-search-report
        """
        return cast("Any", self._caller._call("analytics.search", [], {"provider": provider, "range": range, "from": from_, "to": to, "tz": tz, "dimension": dimension, "value": value, "find": find, "findIn": findIn}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Storefronts:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[StorefrontsListResultItem]:
        """**List storefronts**

        The store's storefronts: each a design of its site, on a theme. One of them is live (`meta.liveId`), which is the one buyers see. A store holds as many as its plan does. `meta.themes` is the themes a new one can start from.

        Needs the `storefronts.read` permission (Read Storefronts).

        Docs: https://docs.shoply.gg/api-reference/storefronts/list-storefronts
        """
        return cast("List[StorefrontsListResultItem]", self._caller._call("storefronts.list", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        name: str,
        theme: Optional[str] = None,
        from_: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[StorefrontsCreateResultItem]:
        """**Create a storefront**

        Adds a storefront as a draft: a theme's starting design, or a copy of one the store already has. Answers the store's storefronts with the new one among them.

        Needs the `storefronts.write` permission (Change Storefronts). Only a key the store's owner made, or an app the owner connected, can call it: one made by somebody on the store's team is refused (`owner_only`).

        Args:
            name: What to call it. Required.
            theme: The theme it starts from, by its ID in `meta.themes`. Left out, it is "simplistic".
            from_: A storefront to copy in place of starting from the theme, by its ID.

        Docs: https://docs.shoply.gg/api-reference/storefronts/create-a-storefront
        """
        return cast("List[StorefrontsCreateResultItem]", self._caller._call("storefronts.create", [], {"name": name, "theme": theme, "from": from_}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def import_(
        self,
        *,
        file: Union[str, "os.PathLike[str]", bytes, BinaryIO],
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Import a storefront**

        Makes a new storefront, as a draft, from one that was exported: the JSON document "Export a storefront" answers under `storefront`, sent as `multipart/form-data` in a field called `file`. Nothing in it is trusted: its design is rebuilt from the theme, and each of its files is checked. One thing wrong refuses all of it, and the refusal names the file. The document can be up to 50 MB, `import_too_large` past it; a storefront whose files are more than that is imported with fewer, and the rest saved after. `meta.imported` says which storefront it became and how many problems its code has to be fixed before it can be published.

        Needs the `storefronts.write` permission (Change Storefronts). Only a key the store's owner made, or an app the owner connected, can call it: one made by somebody on the store's team is refused (`owner_only`).

        Args:
            file: A path on disk, the file's bytes, or a file opened for reading.
            filename: Its name. Left out, the path's own, or "upload".
            content_type: Its type, "image/png". Left out, worked out from the name.

        Docs: https://docs.shoply.gg/api-reference/storefronts/import-a-storefront
        """
        return cast("Any", self._caller._call("storefronts.import", [], {"file": file, "filename": filename, "content_type": content_type}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def export(
        self,
        storefront_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> StorefrontsExportResult:
        """**Export a storefront**

        A storefront to keep, work on or hand on: its design, and every file of its code when it has code of its own, as text. `storefront` in the answer is what "Import a storefront" takes.

        Needs the `storefronts.read` permission (Read Storefronts). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Docs: https://docs.shoply.gg/api-reference/storefronts/export-a-storefront
        """
        return cast("StorefrontsExportResult", self._caller._call("storefronts.export", [storefront_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def rename(
        self,
        storefront_id: str,
        *,
        name: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[StorefrontsRenameResultItem]:
        """**Rename a storefront**

        Changes what a storefront is called. Buyers never see the name. Answers the store's storefronts again.

        Needs the `storefronts.write` permission (Change Storefronts).

        Args:
            name: The new name. Required.

        Docs: https://docs.shoply.gg/api-reference/storefronts/rename-a-storefront
        """
        return cast("List[StorefrontsRenameResultItem]", self._caller._call("storefronts.rename", [storefront_id], {"name": name}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        storefront_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[StorefrontsDeleteResultItem]:
        """**Delete a storefront**

        Removes a storefront that is not the live one. Answers the storefronts that are left.

        Needs the `storefronts.write` permission (Change Storefronts). Only a key the store's owner made, or an app the owner connected, can call it: one made by somebody on the store's team is refused (`owner_only`).

        Docs: https://docs.shoply.gg/api-reference/storefronts/delete-a-storefront
        """
        return cast("List[StorefrontsDeleteResultItem]", self._caller._call("storefronts.delete", [storefront_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setLive(
        self,
        storefront_id: str,
        *,
        publish: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[StorefrontsSetLiveResultItem]:
        """**Make a storefront live**

        Makes this storefront the one buyers see, as it was last published. Answers the store's storefronts again.

        Needs the `storefronts.write` permission (Change Storefronts). Only a key the store's owner made, or an app the owner connected, can call it: one made by somebody on the store's team is refused (`owner_only`).

        Args:
            publish: For a storefront that was never published: publish it as it stands and make it live in one go. A mistake in one of its templates refuses it and names the file. Left out, it is false.

        Docs: https://docs.shoply.gg/api-reference/storefronts/make-a-storefront-live
        """
        return cast("List[StorefrontsSetLiveResultItem]", self._caller._call("storefronts.setLive", [storefront_id], {"publish": publish}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def code(
        self,
        storefront_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> StorefrontsCodeResult:
        """**Get a storefront's code**

        Whether this storefront can be edited as code (`available`), whether it has files of its own yet (`started`), and when it has: every file with its SHA-256 `hash`, what is wrong in the templates (`code.problems`), the count of changes to its files (`code.rev`) and to its design (`version`), which "Publish a storefront's code" takes, and a link to look at the draft on the store's own address for an hour (`preview`: its `url`, with `param` set to `token` in the query string). A file's text is "Get a file", or every file at once in "Export a storefront".

        Needs the `storefronts.read` permission (Read Storefronts).

        Docs: https://docs.shoply.gg/api-reference/storefront-code/get-a-storefronts-code
        """
        return cast("StorefrontsCodeResult", self._caller._call("storefronts.code", [storefront_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def codeStart(
        self,
        storefront_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> StorefrontsCodeStartResult:
        """**Give a storefront files**

        Gives a storefront files of its own, copied from its theme's, as opening the code studio does. Until then it is drawn from its theme's files and follows them as they change. Nothing buyers see changes. Refused with `code_needs_copy` for a storefront from before its theme could be edited as code: make a copy of it ("Create a storefront" with `from`) and work on that. Answers as "Get a storefront's code".

        Needs the `storefronts.write` permission (Change Storefronts).

        Docs: https://docs.shoply.gg/api-reference/storefront-code/give-a-storefront-files
        """
        return cast("StorefrontsCodeStartResult", self._caller._call("storefronts.codeStart", [storefront_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def codeFile(
        self,
        storefront_id: str,
        *,
        path: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> StorefrontsCodeFileResult:
        """**Get a file**

        One file of the storefront's draft, with its text in `content` and its SHA-256 in `hash`. `file_not_found` for a path it does not have.

        Needs the `storefronts.read` permission (Read Storefronts).

        Args:
            path: The file's path, its folder and its name: `pages/index.liquid`, `assets/theme.css`. Required.

        Docs: https://docs.shoply.gg/api-reference/storefront-code/get-a-file
        """
        return cast("StorefrontsCodeFileResult", self._caller._call("storefronts.codeFile", [storefront_id], {"path": path}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def codeSave(
        self,
        storefront_id: str,
        *,
        path: str,
        content: str,
        was: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> StorefrontsCodeSaveResult:
        """**Save a file**

        Saves a file the draft has. Send `was`, the `hash` it had when you read it, and the save is refused with `file_conflict` if it has changed since (in the code studio, say), with the file as it now stands in `file`: left out, it is saved whatever happened in between. Saved to the draft only: buyers see it once it is published. Answers the file as it now stands (`file`) and the whole list again (`code`), with what is now wrong in the templates. What is written counts toward the store's hour of saves, as the code studio's does.

        Needs the `storefronts.write` permission (Change Storefronts).

        Args:
            path: The file's path, its folder and its name: `pages/index.liquid`, `assets/theme.css`. Required.
            content: The file's whole text. Required.
            was: The SHA-256 the file had when you read it.

        Docs: https://docs.shoply.gg/api-reference/storefront-code/save-a-file
        """
        return cast("StorefrontsCodeSaveResult", self._caller._call("storefronts.codeSave", [storefront_id], {"path": path, "content": content, "was": was}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def codeAdd(
        self,
        storefront_id: str,
        *,
        path: str,
        content: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> StorefrontsCodeAddResult:
        """**Add a file**

        Adds a file the draft does not have. Its path has to be in one of the folders a storefront has (`code.folders` in "Get a storefront's code") with that folder's ending. Answers as "Save a file".

        Needs the `storefronts.write` permission (Change Storefronts).

        Args:
            path: The file's path, its folder and its name: `pages/index.liquid`, `assets/theme.css`. Required.
            content: The file's whole text. Required.

        Docs: https://docs.shoply.gg/api-reference/storefront-code/add-a-file
        """
        return cast("StorefrontsCodeAddResult", self._caller._call("storefronts.codeAdd", [storefront_id], {"path": path, "content": content}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def codeDelete(
        self,
        storefront_id: str,
        *,
        path: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> StorefrontsCodeDeleteResult:
        """**Delete a file**

        Takes a file you added out of the draft. A file of the theme's can be changed and put back, never deleted: `file_fixed`.

        Needs the `storefronts.write` permission (Change Storefronts).

        Args:
            path: The file's path, its folder and its name: `pages/index.liquid`, `assets/theme.css`. Required.

        Docs: https://docs.shoply.gg/api-reference/storefront-code/delete-a-file
        """
        return cast("StorefrontsCodeDeleteResult", self._caller._call("storefronts.codeDelete", [storefront_id], {"path": path}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def codeRename(
        self,
        storefront_id: str,
        *,
        from_: str,
        to: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> StorefrontsCodeRenameResult:
        """**Rename a file**

        Moves a file you added to another path. A file of the theme's keeps its name (`file_fixed`).

        Needs the `storefronts.write` permission (Change Storefronts).

        Args:
            from_: Its path now. Required.
            to: Its new path. Required.

        Docs: https://docs.shoply.gg/api-reference/storefront-code/rename-a-file
        """
        return cast("StorefrontsCodeRenameResult", self._caller._call("storefronts.codeRename", [storefront_id], {"from": from_, "to": to}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def codePublish(
        self,
        storefront_id: str,
        *,
        rev: int,
        version: int,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> StorefrontsCodePublishResult:
        """**Publish a storefront's code**

        Puts the draft live, its files and its design together, and makes this storefront the one buyers see, as Publish in the code studio does. Send `rev` and `version` from "Get a storefront's code" as you last read it: if either has moved since (somebody saved in the meantime) it is refused with `draft_conflict`, so you never publish what you have not seen. A mistake in a template refuses it with `code_problems`, the mistakes listed in `problems`.

        Needs the `storefronts.write` permission (Change Storefronts).

        Args:
            rev: The files' count of changes, `code.rev`. Required.
            version: The design's, `version`. Required.

        Docs: https://docs.shoply.gg/api-reference/storefront-code/publish-a-storefronts-code
        """
        return cast("StorefrontsCodePublishResult", self._caller._call("storefronts.codePublish", [storefront_id], {"rev": rev, "version": version}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Routing:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def show(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> RoutingShowResult:
        """**Get Payment Routing**

        `settings`: whether it is on, how a checkout is given a processor (`mode`: `share`, by the share of the month's volume each should have; `order`, the first that can take it; `cheapest`, by the payment fee rates set in Finance), whether a declined card is moved to the next (`retry`), whether a returning buyer goes to their last one (`sticky`), and the health guard (`guard`, pausing a processor with `guardDeclines` of its last `guardWindow` routed payments declined) and `disputeAlert`, the dispute percent the store is told of. `processors` are in the routing in their order, each with its share, caps and order limits, its `state` (`rotation`, `cap`, `paused`, or `off` where it cannot take a card today) and its figures this month. `rules` are checked in their order, `available` is the connected card methods not in the routing yet, and `set` is false where the store has never set it up.

        Needs the `routing.read` permission (Read Payment Routing).

        Docs: https://docs.shoply.gg/api-reference/payment-routing/get-payment-routing
        """
        return cast("RoutingShowResult", self._caller._call("routing.show", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        *,
        enabled: Optional[bool] = None,
        mode: Optional[Literal["share", "order", "cheapest"]] = None,
        retry: Optional[bool] = None,
        sticky: Optional[bool] = None,
        guard: Optional[bool] = None,
        guardDeclines: Optional[int] = None,
        guardWindow: Optional[int] = None,
        disputeAlert: Optional[float] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> RoutingUpdateResult:
        """**Change Payment Routing**

        Changes the settings named and keeps the rest. Switching it on needs a processor in the routing that can take a card today. Answers the whole of Payment Routing again, as "Get Payment Routing" does.

        Needs the `routing.write` permission (Change Payment Routing).

        Args:
            enabled: Whether checkouts are routed.
            mode: How a checkout is given a processor.
            retry: Whether a declined card is moved to the next processor. A card declined as stolen, lost or fake never is.
            sticky: Whether a returning buyer goes to the processor they last paid with.
            guard: Whether a processor whose keys fail, or with too many declines, is paused. The last one in rotation never is.
            guardDeclines: How many of the window's payments declined pause a processor, from 1 to `guardWindow`.
            guardWindow: How many of its last routed payments are judged, from 5 to 200.
            disputeAlert: The percent of a processor's paid orders disputed that the store is told of, once a week at most, above 0 and up to 100. Empty or null for none. Nothing is moved for it.

        Docs: https://docs.shoply.gg/api-reference/payment-routing/change-payment-routing
        """
        return cast("RoutingUpdateResult", self._caller._call("routing.update", [], {"enabled": enabled, "mode": mode, "retry": retry, "sticky": sticky, "guard": guard, "guardDeclines": guardDeclines, "guardWindow": guardWindow, "disputeAlert": disputeAlert}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def addProcessor(
        self,
        *,
        provider: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> RoutingAddProcessorResult:
        """**Add a processor**

        Puts one of the store's connected card methods into the routing, last. The shares are made even again. Answers the whole of Payment Routing again, as "Get Payment Routing" does.

        Needs the `routing.write` permission (Change Payment Routing).

        Args:
            provider: The card method, by its name in "List payment methods". Required.

        Docs: https://docs.shoply.gg/api-reference/payment-routing/add-a-processor
        """
        return cast("RoutingAddProcessorResult", self._caller._call("routing.addProcessor", [], {"provider": provider}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def updateProcessor(
        self,
        provider: str,
        *,
        share: Optional[int] = None,
        capMonth: Optional[float] = None,
        capDay: Optional[float] = None,
        minOrder: Optional[float] = None,
        maxOrder: Optional[float] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> RoutingUpdateProcessorResult:
        """**Change a processor**

        Sets a processor's share and limits, all five at once: one left out is no limit, and a share left out is 0. Caps count every paid order through the method, routed or not, over the UTC month and day. Answers the whole of Payment Routing again, as "Get Payment Routing" does.

        Needs the `routing.write` permission (Change Payment Routing).

        Args:
            share: Its share of the month's volume, as a whole percent from 0 to 100, for `mode` `share`.
            capMonth: The most it is given in a UTC month, in the store's currency. Empty for no cap.
            capDay: The most it is given in a UTC day. No more than `capMonth`.
            minOrder: The smallest order it is given.
            maxOrder: The largest order it is given. At least `minOrder`.

        Docs: https://docs.shoply.gg/api-reference/payment-routing/change-a-processor
        """
        return cast("RoutingUpdateProcessorResult", self._caller._call("routing.updateProcessor", [provider], {"share": share, "capMonth": capMonth, "capDay": capDay, "minOrder": minOrder, "maxOrder": maxOrder}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def removeProcessor(
        self,
        provider: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> RoutingRemoveProcessorResult:
        """**Remove a processor**

        Takes a processor out of the routing, with every rule about it. The method itself stays connected. The last one out switches routing off. Answers the whole of Payment Routing again, as "Get Payment Routing" does.

        Needs the `routing.write` permission (Change Payment Routing).

        Docs: https://docs.shoply.gg/api-reference/payment-routing/remove-a-processor
        """
        return cast("RoutingRemoveProcessorResult", self._caller._call("routing.removeProcessor", [provider], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def resumeProcessor(
        self,
        provider: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> RoutingResumeProcessorResult:
        """**Put a processor back**

        Puts a processor the health guard paused back into the split. A `routing.processor_resumed` webhook is sent. Answers the whole of Payment Routing again, as "Get Payment Routing" does.

        Needs the `routing.write` permission (Change Payment Routing).

        Docs: https://docs.shoply.gg/api-reference/payment-routing/put-a-processor-back
        """
        return cast("RoutingResumeProcessorResult", self._caller._call("routing.resumeProcessor", [provider], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def sortProcessors(
        self,
        *,
        providers: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> RoutingSortProcessorsResult:
        """**Sort processors**

        Sets the processors' order, which `mode` `order` takes the first of. Every processor in the routing, once each. Answers the whole of Payment Routing again, as "Get Payment Routing" does.

        Needs the `routing.write` permission (Change Payment Routing).

        Args:
            providers: The processors' names in their new order. Required.

        Docs: https://docs.shoply.gg/api-reference/payment-routing/sort-processors
        """
        return cast("RoutingSortProcessorsResult", self._caller._call("routing.sortProcessors", [], {"providers": providers}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def addRule(
        self,
        *,
        kind: Literal["country", "amount"],
        action: Literal["only", "never"],
        provider: str,
        countries: Optional[List[str]] = None,
        amountOp: Optional[Literal["over", "under"]] = None,
        amount: Optional[float] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> RoutingAddRuleResult:
        """**Add a rule**

        Adds a rule, last. Every `never` that fits an order leaves its processor out, then the first `only` that fits picks. A store holds up to 50. Answers the whole of Payment Routing again, as "Get Payment Routing" does.

        Needs the `routing.write` permission (Change Payment Routing).

        Args:
            kind: What it looks at: the buyer's country, or the order's amount. Required.
            action: `only`: such orders go to this processor and no other. `never`: they never go to it. Required.
            provider: The processor the rule is about, one in the routing. Required.
            countries: For `country`: up to 100 countries, as two-letter codes.
            amountOp: For `amount`: whether it is about orders over the amount or under it.
            amount: For `amount`: the amount, in the store's currency.

        Docs: https://docs.shoply.gg/api-reference/payment-routing/add-a-rule
        """
        return cast("RoutingAddRuleResult", self._caller._call("routing.addRule", [], {"kind": kind, "action": action, "provider": provider, "countries": countries, "amountOp": amountOp, "amount": amount}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def updateRule(
        self,
        rule_id: str,
        *,
        kind: Literal["country", "amount"],
        action: Literal["only", "never"],
        provider: str,
        countries: Optional[List[str]] = None,
        amountOp: Optional[Literal["over", "under"]] = None,
        amount: Optional[float] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> RoutingUpdateRuleResult:
        """**Change a rule**

        Replaces a rule with the one sent. Answers the whole of Payment Routing again, as "Get Payment Routing" does.

        Needs the `routing.write` permission (Change Payment Routing).

        Args:
            kind: What it looks at: the buyer's country, or the order's amount. Required.
            action: `only`: such orders go to this processor and no other. `never`: they never go to it. Required.
            provider: The processor the rule is about, one in the routing. Required.
            countries: For `country`: up to 100 countries, as two-letter codes.
            amountOp: For `amount`: whether it is about orders over the amount or under it.
            amount: For `amount`: the amount, in the store's currency.

        Docs: https://docs.shoply.gg/api-reference/payment-routing/change-a-rule
        """
        return cast("RoutingUpdateRuleResult", self._caller._call("routing.updateRule", [rule_id], {"kind": kind, "action": action, "provider": provider, "countries": countries, "amountOp": amountOp, "amount": amount}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def deleteRule(
        self,
        rule_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> RoutingDeleteRuleResult:
        """**Delete a rule**

        Answers the whole of Payment Routing again, as "Get Payment Routing" does.

        Needs the `routing.write` permission (Change Payment Routing).

        Docs: https://docs.shoply.gg/api-reference/payment-routing/delete-a-rule
        """
        return cast("RoutingDeleteRuleResult", self._caller._call("routing.deleteRule", [rule_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def sortRules(
        self,
        *,
        ids: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> RoutingSortRulesResult:
        """**Sort rules**

        Sets the order rules are checked in. Every rule, once each. Answers the whole of Payment Routing again, as "Get Payment Routing" does.

        Needs the `routing.write` permission (Change Payment Routing).

        Args:
            ids: The rules' IDs in their new order. Required.

        Docs: https://docs.shoply.gg/api-reference/payment-routing/sort-rules
        """
        return cast("RoutingSortRulesResult", self._caller._call("routing.sortRules", [], {"ids": ids}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class CustomMethods:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CustomMethodsListResultItem]:
        """**List custom payment methods**

        The store's custom payment methods. Where each stands at checkout among the connected methods is `meta.order` in "List payment methods". `meta.max` is how many a store may have, and `meta.variables` the words its instructions and address may fill in.

        Needs the `payments.read` permission (Read Payment Methods).

        Docs: https://docs.shoply.gg/api-reference/custom-payment-methods/list-custom-payment-methods
        """
        return cast("List[CustomMethodsListResultItem]", self._caller._call("customMethods.list", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        kind: Optional[Literal["instructions", "redirect"]] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        instructions: Optional[str] = None,
        redirectUrl: Optional[str] = None,
        asksProof: Optional[bool] = None,
        requiresPicture: Optional[bool] = None,
        enabled: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomMethodsCreateResult:
        """**Create a custom payment method**

        Adds a method, after every other at checkout. A store holds up to 10. Answers the new method.

        Needs the `payments.write` permission (Change Payment Methods). Only a key the store's owner made, or an app the owner connected, can call it: one made by somebody on the store's team is refused (`owner_only`).

        Args:
            kind: `instructions`: the buyer is shown how to pay. `redirect`: the buyer is sent to a page of yours.
            name: What the checkout calls it, up to 60 characters.
            description: A line under its name at checkout, up to 160 characters.
            instructions: For `instructions`: how to pay, in Markdown, up to 300 characters. `{order}`, `{amount}`, `{currency}`, `{email}` and `{store}` are filled in.
            redirectUrl: For `redirect`: the https address the buyer is sent to, up to 1000 characters, with the same variables filled in.
            asksProof: Whether the buyer is asked for a reference or a proof of payment, at least one.
            requiresPicture: Whether a proof of payment is required, whatever else is sent. Needs `asksProof`.
            enabled: Whether the checkout offers it.

        Docs: https://docs.shoply.gg/api-reference/custom-payment-methods/create-a-custom-payment-method
        """
        return cast("CustomMethodsCreateResult", self._caller._call("customMethods.create", [], {"kind": kind, "name": name, "description": description, "instructions": instructions, "redirectUrl": redirectUrl, "asksProof": asksProof, "requiresPicture": requiresPicture, "enabled": enabled}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        method_id: str,
        *,
        kind: Optional[Literal["instructions", "redirect"]] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        instructions: Optional[str] = None,
        redirectUrl: Optional[str] = None,
        asksProof: Optional[bool] = None,
        requiresPicture: Optional[bool] = None,
        enabled: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CustomMethodsUpdateResultItem]:
        """**Update a custom payment method**

        Changes what is sent and keeps the rest. A payment already opened keeps what its buyer was told. Answers the store's custom methods again, as "List custom payment methods" does.

        Needs the `payments.write` permission (Change Payment Methods). Only a key the store's owner made, or an app the owner connected, can call it: one made by somebody on the store's team is refused (`owner_only`).

        Args:
            kind: `instructions`: the buyer is shown how to pay. `redirect`: the buyer is sent to a page of yours.
            name: What the checkout calls it, up to 60 characters.
            description: A line under its name at checkout, up to 160 characters.
            instructions: For `instructions`: how to pay, in Markdown, up to 300 characters. `{order}`, `{amount}`, `{currency}`, `{email}` and `{store}` are filled in.
            redirectUrl: For `redirect`: the https address the buyer is sent to, up to 1000 characters, with the same variables filled in.
            asksProof: Whether the buyer is asked for a reference or a proof of payment, at least one.
            requiresPicture: Whether a proof of payment is required, whatever else is sent. Needs `asksProof`.
            enabled: Whether the checkout offers it.

        Docs: https://docs.shoply.gg/api-reference/custom-payment-methods/update-a-custom-payment-method
        """
        return cast("List[CustomMethodsUpdateResultItem]", self._caller._call("customMethods.update", [method_id], {"kind": kind, "name": name, "description": description, "instructions": instructions, "redirectUrl": redirectUrl, "asksProof": asksProof, "requiresPicture": requiresPicture, "enabled": enabled}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        method_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CustomMethodsDeleteResultItem]:
        """**Delete a custom payment method**

        Its orders keep its name. Its ID is never used again. Answers the store's custom methods again, as "List custom payment methods" does.

        Needs the `payments.write` permission (Change Payment Methods). Only a key the store's owner made, or an app the owner connected, can call it: one made by somebody on the store's team is refused (`owner_only`).

        Docs: https://docs.shoply.gg/api-reference/custom-payment-methods/delete-a-custom-payment-method
        """
        return cast("List[CustomMethodsDeleteResultItem]", self._caller._call("customMethods.delete", [method_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setEnabled(
        self,
        method_id: str,
        *,
        enabled: bool,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CustomMethodsSetEnabledResultItem]:
        """**Switch a custom payment method on or off**

        Answers the store's custom methods again, as "List custom payment methods" does.

        Needs the `payments.write` permission (Change Payment Methods). Only a key the store's owner made, or an app the owner connected, can call it: one made by somebody on the store's team is refused (`owner_only`).

        Args:
            enabled: Whether the checkout offers it. Required.

        Docs: https://docs.shoply.gg/api-reference/custom-payment-methods/switch-a-custom-payment-method-on-or-off
        """
        return cast("List[CustomMethodsSetEnabledResultItem]", self._caller._call("customMethods.setEnabled", [method_id], {"enabled": enabled}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def sort(
        self,
        *,
        ids: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CustomMethodsSortResultItem]:
        """**Sort custom payment methods**

        Puts the methods named in this order, in the places they hold now among the connected ones. To move one between connected methods, use "Sort payment methods" with its ID. Answers the store's custom methods again, as "List custom payment methods" does.

        Needs the `payments.write` permission (Change Payment Methods). Only a key the store's owner made, or an app the owner connected, can call it: one made by somebody on the store's team is refused (`owner_only`).

        Args:
            ids: The methods' IDs in their new order. Required.

        Docs: https://docs.shoply.gg/api-reference/custom-payment-methods/sort-custom-payment-methods
        """
        return cast("List[CustomMethodsSortResultItem]", self._caller._call("customMethods.sort", [], {"ids": ids}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def uploadIcon(
        self,
        method_id: str,
        *,
        file: Union[str, "os.PathLike[str]", bytes, BinaryIO],
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Upload a custom payment method's icon**

        Sent as `multipart/form-data` in a field called `image`. It replaces the one it had. Answers the store's custom methods again, as "List custom payment methods" does.

        Needs the `payments.write` permission (Change Payment Methods). Only a key the store's owner made, or an app the owner connected, can call it: one made by somebody on the store's team is refused (`owner_only`).

        Args:
            file: A path on disk, the file's bytes, or a file opened for reading.
            filename: Its name. Left out, the path's own, or "upload".
            content_type: Its type, "image/png". Left out, worked out from the name.

        Docs: https://docs.shoply.gg/api-reference/custom-payment-methods/upload-a-custom-payment-methods-icon
        """
        return cast("Any", self._caller._call("customMethods.uploadIcon", [method_id], {"file": file, "filename": filename, "content_type": content_type}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def deleteIcon(
        self,
        method_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Remove a custom payment method's icon**

        Answers the store's custom methods again, as "List custom payment methods" does.

        Needs the `payments.write` permission (Change Payment Methods). Only a key the store's owner made, or an app the owner connected, can call it: one made by somebody on the store's team is refused (`owner_only`).

        Docs: https://docs.shoply.gg/api-reference/custom-payment-methods/remove-a-custom-payment-methods-icon
        """
        return cast("Any", self._caller._call("customMethods.deleteIcon", [method_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Products:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        visibility: Optional[Literal["public", "unlisted", "private", "on_hold"]] = None,
        search: Optional[str] = None,
        page: Optional[int] = None,
        perPage: Optional[int] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[ProductsListItem]:
        """**List products**

        The store's products, in the store's own order, each with its variants, pictures, categories and stock counts. A store holds as many as its plan does, up to 1,000: ask for them a page at a time with `page` or `perPage`, and `pages` and `total` say how many there are. With neither, every product, in one answer.

        Needs the `products.read` permission (Read Products).

        Args:
            visibility: Only products with this visibility.
            search: Only products whose name contains this.
            page: Which page of the list. The first is 1. Left out, it is 1.
            perPage: How many a page holds, up to 100. Asking for a page and not saying is 50. Left out, it is 50.

        Docs: https://docs.shoply.gg/api-reference/products/list-products
        """
        return cast("Page[ProductsListItem]", self._caller._call("products.list", [], {"visibility": visibility, "search": search, "page": page, "perPage": perPage}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        name: str,
        variants: List[Dict[str, Any]],
        slug: Optional[str] = None,
        description: Optional[str] = None,
        visibility: Optional[Literal["public", "unlisted", "private", "on_hold"]] = None,
        deliveryInstructions: Optional[str] = None,
        categoryIds: Optional[List[str]] = None,
        isBestSeller: Optional[bool] = None,
        badges: Optional[List[Dict[str, Any]]] = None,
        features: Optional[List[Dict[str, Any]]] = None,
        blockedPaymentMethods: Optional[List[str]] = None,
        paymentFees: Optional[Dict[str, Any]] = None,
        salesWindow: Optional[Literal["all", "1h", "6h", "12h", "24h", "7d", "30d"]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        seoTitle: Optional[str] = None,
        seoDescription: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ProductsCreateResult:
        """**Create a product**

        Adds a product with its variants. A store holds as many products as its plan does. Stock is added afterwards, a variant at a time, with the variant IDs in the answer.

        A refusal names the field, and for a variant its place in the list: `variants.0.price`.

        Needs the `products.write` permission (Change Products).

        Args:
            name: The product's name. Required.
            variants: The product's options, 1 to 100 of them, in the order buyers see them. A variant of the product that is not in this list is removed. Required.
            slug: The last part of its address on the storefront. Left out, it is made from the name.
            description: What the product page says. Plain text with a few marks: a line that starts with `#` is a heading, one that starts with `-` is a point of a list, a blank line ends a paragraph, and `**bold**` and backticks for code work inside a line.
            visibility: `public` is listed and can be bought. `unlisted` can be bought by whoever has its link. `private` cannot be bought. `on_hold` is listed as a public product is and cannot be bought: its page says it is on hold, and every checkout refuses it. Left out, it is "public".
            deliveryInstructions: Text sent to the buyer with every variant of the product once the order is paid, whatever the variant delivers, up to 5,000 characters. A variant's own instructions are sent after it. Empty is none. Left out on an update, it stays as it is.
            categoryIds: The categories it is in. Left out on an update, they stay as they are.
            isBestSeller: Whether the storefront marks it as a best seller. Left out, it is false.
            badges: Up to 3 short labels on the product. Left out on an update, they stay as they are.
            features: What the product does, as a list. Each entry is a feature on its own or a named group of features. Up to 500 features and 30 groups. Left out on an update, they stay as they are.
            blockedPaymentMethods: Payment methods the product cannot be bought with, by their names in the payment methods list. Left out on an update, they stay as they are.
            paymentFees: What a payment method adds to this product's price: a payment method's name, and under it `percent` and `fixed`. A fee can only add. Left out on an update, the fees stay as they are.
            salesWindow: The period the storefront's "sold" figure for this product counts. Left out, it is "all".
            metadata: Anything of your own to keep with the product, as JSON. Shoply stores it and does nothing with it. It is answered as text.
            seoTitle: The product's own title in search results, up to 70 characters. Empty is its name.
            seoDescription: Its own description in search results, up to 200 characters. Empty is its description.

        Docs: https://docs.shoply.gg/api-reference/products/create-a-product
        """
        return cast("ProductsCreateResult", self._caller._call("products.create", [], {"name": name, "variants": variants, "slug": slug, "description": description, "visibility": visibility, "deliveryInstructions": deliveryInstructions, "categoryIds": categoryIds, "isBestSeller": isBestSeller, "badges": badges, "features": features, "blockedPaymentMethods": blockedPaymentMethods, "paymentFees": paymentFees, "salesWindow": salesWindow, "metadata": metadata, "seoTitle": seoTitle, "seoDescription": seoDescription}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def show(
        self,
        product_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ProductsShowResult:
        """**Get a product**

        One product, with everything its editor shows.

        Needs the `products.read` permission (Read Products).

        Docs: https://docs.shoply.gg/api-reference/products/get-a-product
        """
        return cast("ProductsShowResult", self._caller._call("products.show", [product_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        product_id: str,
        *,
        name: str,
        variants: List[Dict[str, Any]],
        slug: Optional[str] = None,
        description: Optional[str] = None,
        visibility: Optional[Literal["public", "unlisted", "private", "on_hold"]] = None,
        deliveryInstructions: Optional[str] = None,
        categoryIds: Optional[List[str]] = None,
        isBestSeller: Optional[bool] = None,
        badges: Optional[List[Dict[str, Any]]] = None,
        features: Optional[List[Dict[str, Any]]] = None,
        blockedPaymentMethods: Optional[List[str]] = None,
        paymentFees: Optional[Dict[str, Any]] = None,
        salesWindow: Optional[Literal["all", "1h", "6h", "12h", "24h", "7d", "30d"]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        seoTitle: Optional[str] = None,
        seoDescription: Optional[str] = None,
        expectedUpdatedAt: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ProductsUpdateResult:
        """**Update a product**

        Saves the product whole, as its editor does: send every field as it should be. `variants` is the complete list. An entry with an `id` changes that variant, an entry without one is added, and a variant left out is removed with its unsold stock. A variant buyers have received license keys from cannot be removed.

        Read the product first and send it back changed. The fields that say "stay as they are" are the only ones that may be left out.

        Needs the `products.write` permission (Change Products).

        Args:
            name: The product's name. Required.
            variants: The product's options, 1 to 100 of them, in the order buyers see them. A variant of the product that is not in this list is removed. Required.
            slug: The last part of its address on the storefront. Left out, it is made from the name.
            description: What the product page says. Plain text with a few marks: a line that starts with `#` is a heading, one that starts with `-` is a point of a list, a blank line ends a paragraph, and `**bold**` and backticks for code work inside a line.
            visibility: `public` is listed and can be bought. `unlisted` can be bought by whoever has its link. `private` cannot be bought. `on_hold` is listed as a public product is and cannot be bought: its page says it is on hold, and every checkout refuses it. Left out, it is "public".
            deliveryInstructions: Text sent to the buyer with every variant of the product once the order is paid, whatever the variant delivers, up to 5,000 characters. A variant's own instructions are sent after it. Empty is none. Left out on an update, it stays as it is.
            categoryIds: The categories it is in. Left out on an update, they stay as they are.
            isBestSeller: Whether the storefront marks it as a best seller. Left out, it is false.
            badges: Up to 3 short labels on the product. Left out on an update, they stay as they are.
            features: What the product does, as a list. Each entry is a feature on its own or a named group of features. Up to 500 features and 30 groups. Left out on an update, they stay as they are.
            blockedPaymentMethods: Payment methods the product cannot be bought with, by their names in the payment methods list. Left out on an update, they stay as they are.
            paymentFees: What a payment method adds to this product's price: a payment method's name, and under it `percent` and `fixed`. A fee can only add. Left out on an update, the fees stay as they are.
            salesWindow: The period the storefront's "sold" figure for this product counts. Left out, it is "all".
            metadata: Anything of your own to keep with the product, as JSON. Shoply stores it and does nothing with it. It is answered as text.
            seoTitle: The product's own title in search results, up to 70 characters. Empty is its name.
            seoDescription: Its own description in search results, up to 200 characters. Empty is its description.
            expectedUpdatedAt: The `updatedAt` you last read. Sent, the change is refused with `stale_write` if the record has changed since. Left out, it is saved whatever happened in between.

        Docs: https://docs.shoply.gg/api-reference/products/update-a-product
        """
        return cast("ProductsUpdateResult", self._caller._call("products.update", [product_id], {"name": name, "variants": variants, "slug": slug, "description": description, "visibility": visibility, "deliveryInstructions": deliveryInstructions, "categoryIds": categoryIds, "isBestSeller": isBestSeller, "badges": badges, "features": features, "blockedPaymentMethods": blockedPaymentMethods, "paymentFees": paymentFees, "salesWindow": salesWindow, "metadata": metadata, "seoTitle": seoTitle, "seoDescription": seoDescription, "expectedUpdatedAt": expectedUpdatedAt}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        product_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Delete a product**

        Removes the product with its variants, pictures and unsold stock. Refused for a product buyers have received license keys from, since those keys are part of their orders: set its visibility to `private` instead.

        Needs the `products.write` permission (Change Products).

        Docs: https://docs.shoply.gg/api-reference/products/delete-a-product
        """
        return cast("Any", self._caller._call("products.delete", [product_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setVisibility(
        self,
        product_id: str,
        *,
        visibility: Literal["public", "unlisted", "private", "on_hold"],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ProductsSetVisibilityResult:
        """**Set a product's visibility**

        Changes who can see and buy the product, without sending the rest of it.

        Needs the `products.write` permission (Change Products).

        Args:
            visibility: The new visibility. Required.

        Docs: https://docs.shoply.gg/api-reference/products/set-a-products-visibility
        """
        return cast("ProductsSetVisibilityResult", self._caller._call("products.setVisibility", [product_id], {"visibility": visibility}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def sort(
        self,
        *,
        productIds: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ProductsSortResult:
        """**Sort products**

        Sets the order products are listed in, on the storefront and everywhere else.

        Needs the `products.write` permission (Change Products).

        Args:
            productIds: The products' IDs in their new order. Required.

        Docs: https://docs.shoply.gg/api-reference/products/sort-products
        """
        return cast("ProductsSortResult", self._caller._call("products.sort", [], {"productIds": productIds}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def bulkUpdate(
        self,
        *,
        productIds: List[str],
        visibility: Optional[Literal["public", "unlisted", "private", "on_hold"]] = None,
        isBestSeller: Optional[bool] = None,
        paymentMethods: Optional[Dict[str, Any]] = None,
        deliveryInstructions: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ProductsBulkUpdateResult:
        """**Change many products**

        One change made to many products. Only what is sent changes.

        Needs the `products.write` permission (Change Products).

        Args:
            productIds: The products, by ID. Up to 250. Required.
            visibility: A visibility for all of them.
            isBestSeller: Whether all of them are marked as best sellers.
            paymentMethods: A payment method's name, and `block` or `allow`. `block` adds the method to each product's blocked list. `allow` takes it off the product and off every variant of it.
            deliveryInstructions: Instructions for every variant of all of them, up to 5,000 characters, in place of what each has. Empty takes them off. A variant's own instructions are not touched.

        Docs: https://docs.shoply.gg/api-reference/products/change-many-products
        """
        return cast("ProductsBulkUpdateResult", self._caller._call("products.bulkUpdate", [], {"productIds": productIds, "visibility": visibility, "isBestSeller": isBestSeller, "paymentMethods": paymentMethods, "deliveryInstructions": deliveryInstructions}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def bulkDelete(
        self,
        *,
        productIds: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Delete many products**

        Deletes each product as deleting one does. A product buyers have received license keys from is kept, and the answer names the ones that stayed.

        Needs the `products.write` permission (Change Products).

        Args:
            productIds: The products, by ID. Up to 250. Required.

        Docs: https://docs.shoply.gg/api-reference/products/delete-many-products
        """
        return cast("Any", self._caller._call("products.bulkDelete", [], {"productIds": productIds}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class ProductImages:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def upload(
        self,
        product_id: str,
        *,
        file: Union[str, "os.PathLike[str]", bytes, BinaryIO],
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Upload a product picture**

        Adds a picture to the product, sent as `multipart/form-data` in a field called `image`. A product holds as many as its store's plan does. The first one uploaded is the one listings show.

        Needs the `products.write` permission (Change Products).

        Args:
            file: A path on disk, the file's bytes, or a file opened for reading.
            filename: Its name. Left out, the path's own, or "upload".
            content_type: Its type, "image/png". Left out, worked out from the name.

        Docs: https://docs.shoply.gg/api-reference/product-pictures/upload-a-product-picture
        """
        return cast("Any", self._caller._call("productImages.upload", [product_id], {"file": file, "filename": filename, "content_type": content_type}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def sort(
        self,
        product_id: str,
        *,
        imageIds: Optional[List[str]] = None,
        imageId: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Sort a product's pictures**

        Sets the order of the product's pictures, or moves one to the front. The first picture is the one listings show. Send one of the two fields.

        Needs the `products.write` permission (Change Products).

        Args:
            imageIds: Every picture's ID, in the new order.
            imageId: One picture to move to the front, leaving the rest as they are.

        Docs: https://docs.shoply.gg/api-reference/product-pictures/sort-a-products-pictures
        """
        return cast("Any", self._caller._call("productImages.sort", [product_id], {"imageIds": imageIds, "imageId": imageId}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        product_id: str,
        image_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Delete a product picture**

        Removes one picture from the product.

        Needs the `products.write` permission (Change Products).

        Docs: https://docs.shoply.gg/api-reference/product-pictures/delete-a-product-picture
        """
        return cast("Any", self._caller._call("productImages.delete", [product_id, image_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Stock:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def listKeys(
        self,
        variant_id: str,
        *,
        page: Optional[int] = None,
        perPage: Optional[int] = None,
        search: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[StockListKeysItem]:
        """**List a variant's license keys**

        The license keys a variant has in stock: the unsold ones and nothing else. A key that was delivered belongs to its order and is read there.

        Needs the `stock.read` permission (Read Stock).

        Args:
            page: Which page of the list. The first is 1. Left out, it is 1.
            perPage: How many a page holds, up to 5,000. Left out, it is 100.
            search: Only keys that contain this.

        Docs: https://docs.shoply.gg/api-reference/stock/list-a-variants-license-keys
        """
        return cast("Page[StockListKeysItem]", self._caller._call("stock.listKeys", [variant_id], {"page": page, "perPage": perPage, "search": search}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def addKeys(
        self,
        variant_id: str,
        *,
        keys: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> StockAddKeysResult:
        """**Add license keys**

        Adds license keys to a variant's stock, up to 5,000 in one request. A variant and a store each hold as many unsold keys as the store's plan does.

        A key sent twice is stocked twice, which is how one key is sold to several buyers. `duplicates` in the answer counts the ones that matched stock the variant already had, so sending the same batch a second time by mistake shows.

        Needs the `stock.write` permission (Change Stock).

        Args:
            keys: The keys, one an entry, each up to 500 characters with no line break in it. Required.

        Docs: https://docs.shoply.gg/api-reference/stock/add-license-keys
        """
        return cast("StockAddKeysResult", self._caller._call("stock.addKeys", [variant_id], {"keys": keys}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def replaceKeys(
        self,
        variant_id: str,
        *,
        keys: List[str],
        expectedAvailable: Optional[int] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Replace a variant's license keys**

        Makes the variant's unsold stock exactly the keys sent. Keys already delivered are not touched: they are order history, not stock. Up to 5,000 keys, and only for a variant with no more than that in stock: one with more is refused with `validation_error`, and its keys are added and deleted instead.

        Needs the `stock.write` permission (Change Stock).

        Args:
            keys: The keys the variant is to have in stock, one an entry. An empty list empties the stock. Required.
            expectedAvailable: How many unsold keys you last read. Sent, the change is refused with `stale_write` if that number has changed, so a key sold in the meantime is not put back.

        Docs: https://docs.shoply.gg/api-reference/stock/replace-a-variants-license-keys
        """
        return cast("Any", self._caller._call("stock.replaceKeys", [variant_id], {"keys": keys, "expectedAvailable": expectedAvailable}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def deleteKeys(
        self,
        variant_id: str,
        *,
        ids: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> StockDeleteKeysResult:
        """**Delete license keys**

        Deletes the unsold keys among the ones named. `removed` in the answer can be lower than the number sent: a key sold in the meantime stays with its order.

        Needs the `stock.write` permission (Change Stock).

        Args:
            ids: The keys to delete, by ID. Required.

        Docs: https://docs.shoply.gg/api-reference/stock/delete-license-keys
        """
        return cast("StockDeleteKeysResult", self._caller._call("stock.deleteKeys", [variant_id], {"ids": ids}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def deleteKey(
        self,
        variant_id: str,
        key_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Delete a license key**

        Deletes one unsold key. Refused for a key that has been sold.

        Needs the `stock.write` permission (Change Stock).

        Docs: https://docs.shoply.gg/api-reference/stock/delete-a-license-key
        """
        return cast("Any", self._caller._call("stock.deleteKey", [variant_id, key_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def listFiles(
        self,
        variant_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Union[List[Any], Dict[str, Any]]:
        """**List a variant's files**

        The files a variant delivers to its buyers.

        Needs the `stock.read` permission (Read Stock).

        Docs: https://docs.shoply.gg/api-reference/stock/list-a-variants-files
        """
        return cast("Union[List[Any], Dict[str, Any]]", self._caller._call("stock.listFiles", [variant_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def addFile(
        self,
        variant_id: str,
        *,
        name: str,
        size: int,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Start a file upload**

        The first of three steps to give a variant a file to deliver. This one says what the file is and answers a signed address to send it to. Then send the file itself to that address with a `PUT`. Then call "Finish a file upload".

        How many files a variant and a store hold, how large one may be and how much a store holds in all are the store's plan's. Accepted: ZIP, RAR, 7z, PDF, MP4, MP3, WAV, EPUB, EXE, DMG, MSI and APK.

        Needs the `stock.write` permission (Change Stock).

        Args:
            name: The file's name, with its ending. Buyers download it under this name. Required.
            size: Its size in bytes. Required.

        Docs: https://docs.shoply.gg/api-reference/stock/start-a-file-upload
        """
        return cast("Any", self._caller._call("stock.addFile", [variant_id], {"name": name, "size": size}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def finishFile(
        self,
        variant_id: str,
        file_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Finish a file upload**

        The last step of adding a file: says the file has been sent. Shoply checks it arrived and is the size that was said, and from then on buyers of the variant receive it.

        Needs the `stock.write` permission (Change Stock).

        Docs: https://docs.shoply.gg/api-reference/stock/finish-a-file-upload
        """
        return cast("Any", self._caller._call("stock.finishFile", [variant_id, file_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def deleteFile(
        self,
        variant_id: str,
        file_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Delete a file**

        Removes a file from the variant. Buyers who already have a link to it can no longer download it.

        Needs the `stock.write` permission (Change Stock).

        Docs: https://docs.shoply.gg/api-reference/stock/delete-a-file
        """
        return cast("Any", self._caller._call("stock.deleteFile", [variant_id, file_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Categories:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        visibility: Optional[Literal["public", "unlisted", "private"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CategoriesListResultItem]:
        """**List categories**

        Every category the store has, in the store's own order, each with the products in it. A store holds as many as its plan does, 500 at most, so the list is not paged.

        Needs the `categories.read` permission (Read Categories).

        Args:
            visibility: Only categories with this visibility.

        Docs: https://docs.shoply.gg/api-reference/categories/list-categories
        """
        return cast("List[CategoriesListResultItem]", self._caller._call("categories.list", [], {"visibility": visibility}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        name: str,
        slug: Optional[str] = None,
        description: Optional[str] = None,
        visibility: Optional[Literal["public", "unlisted", "private"]] = None,
        isPopular: Optional[bool] = None,
        productIds: Optional[List[str]] = None,
        seoTitle: Optional[str] = None,
        seoDescription: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CategoriesCreateResult:
        """**Create a category**

        Adds a category, with the products that go in it. A store holds as many as its plan does.

        Needs the `categories.write` permission (Change Categories).

        Args:
            name: The category's name. Required.
            slug: The last part of its address on the storefront. Left out, it is made from the name.
            description: What the category's page says under its name.
            visibility: `public` is listed on the storefront. `unlisted` is reached by its link. `private` is not shown. Left out, it is "public".
            isPopular: Whether themes that feature a category may feature this one. Left out, it is false.
            productIds: The products in it, in the order the category lists them.
            seoTitle: The category's own title in search results, up to 70 characters. Empty is its name.
            seoDescription: Its own description in search results, up to 200 characters. Empty is its description.

        Docs: https://docs.shoply.gg/api-reference/categories/create-a-category
        """
        return cast("CategoriesCreateResult", self._caller._call("categories.create", [], {"name": name, "slug": slug, "description": description, "visibility": visibility, "isPopular": isPopular, "productIds": productIds, "seoTitle": seoTitle, "seoDescription": seoDescription}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        category_id: str,
        *,
        name: str,
        slug: Optional[str] = None,
        description: Optional[str] = None,
        visibility: Optional[Literal["public", "unlisted", "private"]] = None,
        isPopular: Optional[bool] = None,
        productIds: Optional[List[str]] = None,
        seoTitle: Optional[str] = None,
        seoDescription: Optional[str] = None,
        expectedUpdatedAt: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CategoriesUpdateResult:
        """**Update a category**

        Saves the category whole: send every field as it should be. `productIds` is the exception: left out, the products in the category stay as they are.

        Needs the `categories.write` permission (Change Categories).

        Args:
            name: The category's name. Required.
            slug: The last part of its address on the storefront. Left out, it is made from the name.
            description: What the category's page says under its name.
            visibility: `public` is listed on the storefront. `unlisted` is reached by its link. `private` is not shown. Left out, it is "public".
            isPopular: Whether themes that feature a category may feature this one. Left out, it is false.
            productIds: The products in it, in the order the category lists them.
            seoTitle: The category's own title in search results, up to 70 characters. Empty is its name.
            seoDescription: Its own description in search results, up to 200 characters. Empty is its description.
            expectedUpdatedAt: The `updatedAt` you last read. Sent, the change is refused with `stale_write` if the record has changed since. Left out, it is saved whatever happened in between.

        Docs: https://docs.shoply.gg/api-reference/categories/update-a-category
        """
        return cast("CategoriesUpdateResult", self._caller._call("categories.update", [category_id], {"name": name, "slug": slug, "description": description, "visibility": visibility, "isPopular": isPopular, "productIds": productIds, "seoTitle": seoTitle, "seoDescription": seoDescription, "expectedUpdatedAt": expectedUpdatedAt}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        category_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CategoriesDeleteResult:
        """**Delete a category**

        Removes the category. The products that were in it are not deleted.

        Needs the `categories.write` permission (Change Categories).

        Docs: https://docs.shoply.gg/api-reference/categories/delete-a-category
        """
        return cast("CategoriesDeleteResult", self._caller._call("categories.delete", [category_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def sort(
        self,
        *,
        categoryIds: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CategoriesSortResult:
        """**Sort categories**

        Sets the order categories are listed in.

        Needs the `categories.write` permission (Change Categories).

        Args:
            categoryIds: The categories' IDs in their new order. Required.

        Docs: https://docs.shoply.gg/api-reference/categories/sort-categories
        """
        return cast("CategoriesSortResult", self._caller._call("categories.sort", [], {"categoryIds": categoryIds}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def uploadImage(
        self,
        category_id: str,
        *,
        file: Union[str, "os.PathLike[str]", bytes, BinaryIO],
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Upload a category's picture**

        Gives the category its one picture, sent as `multipart/form-data` in a field called `image`. A picture it already had is replaced.

        Needs the `categories.write` permission (Change Categories).

        Args:
            file: A path on disk, the file's bytes, or a file opened for reading.
            filename: Its name. Left out, the path's own, or "upload".
            content_type: Its type, "image/png". Left out, worked out from the name.

        Docs: https://docs.shoply.gg/api-reference/categories/upload-a-categorys-picture
        """
        return cast("Any", self._caller._call("categories.uploadImage", [category_id], {"file": file, "filename": filename, "content_type": content_type}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def deleteImage(
        self,
        category_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Delete a category's picture**

        Removes the category's picture.

        Needs the `categories.write` permission (Change Categories).

        Docs: https://docs.shoply.gg/api-reference/categories/delete-a-categorys-picture
        """
        return cast("Any", self._caller._call("categories.deleteImage", [category_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Upsells:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        range: Optional[str] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[UpsellsListResultItem]:
        """**List upsells**

        Every upsell the store has, a kind at a time in the store's order, with the times each was shown, the paid orders that took it and what those lines came to over a period. A store holds as many as its plan does.

        Needs the `upsells.read` permission (Read Upsells).

        Args:
            range: The period: `today`, `7d`, `30d`, `this_month`, `last_month`, `this_year`, `custom` with `from` and `to`, or `all`. Left out, it is "30d".
            from_: With `range` `custom`: the first day, as YYYY-MM-DD.
            to: With `range` `custom`: the last day, as YYYY-MM-DD.
            tz: The time zone the days are read in, as an IANA name. Left out, UTC.

        Docs: https://docs.shoply.gg/api-reference/upsells/list-upsells
        """
        return cast("List[UpsellsListResultItem]", self._caller._call("upsells.list", [], {"range": range, "from": from_, "to": to, "tz": tz}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        kind: Literal["addon", "cart", "checkout", "together", "upgrade"],
        tz: Optional[str] = None,
        name: Optional[str] = None,
        sells: Optional[Literal["extra", "product"]] = None,
        productId: Optional[str] = None,
        variantId: Optional[str] = None,
        price: Optional[float] = None,
        cost: Optional[float] = None,
        message: Optional[str] = None,
        offered: Optional[Literal["optional", "ticked", "included"]] = None,
        charged: Optional[Literal["order", "item"]] = None,
        trigger: Optional[Literal["product", "category", "amount"]] = None,
        minSubtotal: Optional[float] = None,
        discountType: Optional[Literal["none", "percent", "amount"]] = None,
        discountValue: Optional[float] = None,
        targets: Optional[List[Dict[str, Any]]] = None,
        words: Optional[str] = None,
        startsAt: Optional[str] = None,
        endsAt: Optional[str] = None,
        firstOrders: Optional[bool] = None,
        hideOwned: Optional[bool] = None,
        enabled: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> UpsellsCreateResult:
        """**Create an upsell**

        Adds an upsell of one kind. What it needs depends on the kind: see each field. A store holds as many as its plan does.

        Needs the `upsells.write` permission (Change Upsells).

        Args:
            kind: What kind of upsell it is. Set when it is made, and never changes. Required.
            tz: The time zone `startsAt` and `endsAt` are read in when they name none, as an IANA name. Left out, UTC.
            name: Up to 80 characters. An add-on that is a plain extra needs one: it is what the buyer reads.
            sells: An add-on only: a plain extra, or one of the store's products. Left out, it is "product".
            productId: What it sells, or for `together` what is shown. Not for a plain extra.
            variantId: Which of the product's variants. Optional for `together`.
            price: An add-on's price as an add-on, in the store's currency.
            cost: A plain extra's cost for one, for Finance.
            message: A plain extra's message to the buyer after payment, up to 2,000 characters.
            offered: An add-on: the buyer ticks it, it is ticked for them, or it is always in the order. Left out, it is "optional".
            charged: An add-on: once an order, or for each unit of its line. Left out, it is "order".
            trigger: A cart or checkout offer: what it asks for in the cart. Left out, it is "product".
            minSubtotal: With `trigger` `amount`: the cart total it asks for.
            discountType: A cart, checkout or upgrade offer: what it takes off its product, on that order only. Left out, it is "none".
            discountValue: How much: above 0 and up to 100 for `percent`, an amount for `amount`.
            targets: Up to 100. What an add-on is offered with (products or categories), what a cart or checkout offer asks for, what `together` is shown under and what an upgrade replaces (products).
            words: The line over it where the buyer meets it, up to 80 characters. Left out, the buyer's language's own words.
            startsAt: When it starts, as a date and time. Left out, now.
            endsAt: When it ends, as a date and time. Left out, never.
            firstOrders: A checkout offer only, since the checkout is where the buyer is known: offered only to a buyer who has never paid at the store. Left out, it is false.
            hideOwned: A checkout offer only: not offered to a buyer who has bought it before. Left out, it is false.
            enabled: Whether it is offered. Left out, it is true.

        Docs: https://docs.shoply.gg/api-reference/upsells/create-an-upsell
        """
        return cast("UpsellsCreateResult", self._caller._call("upsells.create", [], {"kind": kind, "tz": tz, "name": name, "sells": sells, "productId": productId, "variantId": variantId, "price": price, "cost": cost, "message": message, "offered": offered, "charged": charged, "trigger": trigger, "minSubtotal": minSubtotal, "discountType": discountType, "discountValue": discountValue, "targets": targets, "words": words, "startsAt": startsAt, "endsAt": endsAt, "firstOrders": firstOrders, "hideOwned": hideOwned, "enabled": enabled}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def sort(
        self,
        *,
        kind: Literal["addon", "cart", "checkout", "together", "upgrade"],
        ids: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> UpsellsSortResult:
        """**Sort upsells**

        Puts one kind's upsells in a new order. The first that applies is the one shown where only one is.

        Needs the `upsells.write` permission (Change Upsells).

        Args:
            kind: Which kind. Required.
            ids: Its upsells, in their new order. Required.

        Docs: https://docs.shoply.gg/api-reference/upsells/sort-upsells
        """
        return cast("UpsellsSortResult", self._caller._call("upsells.sort", [], {"kind": kind, "ids": ids}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def settings(
        self,
        *,
        boughtTogetherAuto: bool,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> UpsellsSettingsResult:
        """**Change upsell settings**

        Whether a product's page also shows what the store's own orders most often have with it.

        Needs the `upsells.write` permission (Change Upsells).

        Args:
            boughtTogetherAuto: Whether what is bought together is worked out from the store's orders too. Required.

        Docs: https://docs.shoply.gg/api-reference/upsells/change-upsell-settings
        """
        return cast("UpsellsSettingsResult", self._caller._call("upsells.settings", [], {"boughtTogetherAuto": boughtTogetherAuto}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        upsell_id: str,
        *,
        kind: Literal["addon", "cart", "checkout", "together", "upgrade"],
        tz: Optional[str] = None,
        name: Optional[str] = None,
        sells: Optional[Literal["extra", "product"]] = None,
        productId: Optional[str] = None,
        variantId: Optional[str] = None,
        price: Optional[float] = None,
        cost: Optional[float] = None,
        message: Optional[str] = None,
        offered: Optional[Literal["optional", "ticked", "included"]] = None,
        charged: Optional[Literal["order", "item"]] = None,
        trigger: Optional[Literal["product", "category", "amount"]] = None,
        minSubtotal: Optional[float] = None,
        discountType: Optional[Literal["none", "percent", "amount"]] = None,
        discountValue: Optional[float] = None,
        targets: Optional[List[Dict[str, Any]]] = None,
        words: Optional[str] = None,
        startsAt: Optional[str] = None,
        endsAt: Optional[str] = None,
        firstOrders: Optional[bool] = None,
        hideOwned: Optional[bool] = None,
        enabled: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> UpsellsUpdateResult:
        """**Update an upsell**

        Saves the upsell whole: send every field as it should be, not only what changed. Its kind does not change.

        Needs the `upsells.write` permission (Change Upsells).

        Args:
            kind: What kind of upsell it is. Set when it is made, and never changes. Required.
            tz: The time zone `startsAt` and `endsAt` are read in when they name none, as an IANA name. Left out, UTC.
            name: Up to 80 characters. An add-on that is a plain extra needs one: it is what the buyer reads.
            sells: An add-on only: a plain extra, or one of the store's products. Left out, it is "product".
            productId: What it sells, or for `together` what is shown. Not for a plain extra.
            variantId: Which of the product's variants. Optional for `together`.
            price: An add-on's price as an add-on, in the store's currency.
            cost: A plain extra's cost for one, for Finance.
            message: A plain extra's message to the buyer after payment, up to 2,000 characters.
            offered: An add-on: the buyer ticks it, it is ticked for them, or it is always in the order. Left out, it is "optional".
            charged: An add-on: once an order, or for each unit of its line. Left out, it is "order".
            trigger: A cart or checkout offer: what it asks for in the cart. Left out, it is "product".
            minSubtotal: With `trigger` `amount`: the cart total it asks for.
            discountType: A cart, checkout or upgrade offer: what it takes off its product, on that order only. Left out, it is "none".
            discountValue: How much: above 0 and up to 100 for `percent`, an amount for `amount`.
            targets: Up to 100. What an add-on is offered with (products or categories), what a cart or checkout offer asks for, what `together` is shown under and what an upgrade replaces (products).
            words: The line over it where the buyer meets it, up to 80 characters. Left out, the buyer's language's own words.
            startsAt: When it starts, as a date and time. Left out, now.
            endsAt: When it ends, as a date and time. Left out, never.
            firstOrders: A checkout offer only, since the checkout is where the buyer is known: offered only to a buyer who has never paid at the store. Left out, it is false.
            hideOwned: A checkout offer only: not offered to a buyer who has bought it before. Left out, it is false.
            enabled: Whether it is offered. Left out, it is true.

        Docs: https://docs.shoply.gg/api-reference/upsells/update-an-upsell
        """
        return cast("UpsellsUpdateResult", self._caller._call("upsells.update", [upsell_id], {"kind": kind, "tz": tz, "name": name, "sells": sells, "productId": productId, "variantId": variantId, "price": price, "cost": cost, "message": message, "offered": offered, "charged": charged, "trigger": trigger, "minSubtotal": minSubtotal, "discountType": discountType, "discountValue": discountValue, "targets": targets, "words": words, "startsAt": startsAt, "endsAt": endsAt, "firstOrders": firstOrders, "hideOwned": hideOwned, "enabled": enabled}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        upsell_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> UpsellsDeleteResult:
        """**Delete an upsell**

        Removes the upsell. Orders that took it keep their lines as they were.

        Needs the `upsells.write` permission (Change Upsells).

        Docs: https://docs.shoply.gg/api-reference/upsells/delete-an-upsell
        """
        return cast("UpsellsDeleteResult", self._caller._call("upsells.delete", [upsell_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setEnabled(
        self,
        upsell_id: str,
        *,
        enabled: bool,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> UpsellsSetEnabledResult:
        """**Switch an upsell on or off**

        Changes whether the upsell is offered, without sending the rest of it.

        Needs the `upsells.write` permission (Change Upsells).

        Args:
            enabled: Whether it is offered. Required.

        Docs: https://docs.shoply.gg/api-reference/upsells/switch-an-upsell-on-or-off
        """
        return cast("UpsellsSetEnabledResult", self._caller._call("upsells.setEnabled", [upsell_id], {"enabled": enabled}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Subscriptions:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        page: Optional[int] = None,
        show: Optional[Literal["all", "active", "attention", "paused", "cancelling", "ended"]] = None,
        variant: Optional[str] = None,
        search: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[SubscriptionsListItem]:
        """**List subscriptions**

        The store's subscriptions, newest first, 25 a page. A subscription's `status` is `active`, `renewal_due` (its renewal is made and waits to be paid), `past_due` (the period ran out unpaid: it ends after the store's grace days), `paused`, `cancelling` (it ends when what was paid for runs out), `cancelled` or `expired`. `renewsWith` is the card kept for one paid through Stripe, NMI, Authorize.net, Tagada, Mollie, MONEI, Adyen or Square (`provider`, `name`, `label` once named, and `canChange`, whether its buyer may give another on Stripe's own page), and null for one renewed by email; `autoRenews` says whether its next renewal is charged to it by itself. `meta.figures` is what the dashboard shows over the list, `meta.attention` the past due ones, and `meta.plans` which options are sold as subscriptions.

        Needs the `subscriptions.read` permission (Read Subscriptions).

        Args:
            page: Which page of the list. The first is 1. Left out, it is 1.
            show: Only these: running and not cancelling, past due, paused, cancelling, or ended (cancelled and expired). Left out, it is "all".
            variant: Only subscriptions to this option, by its ID.
            search: Part of a buyer's email.

        Docs: https://docs.shoply.gg/api-reference/subscriptions/list-subscriptions
        """
        return cast("Page[SubscriptionsListItem]", self._caller._call("subscriptions.list", [], {"page": page, "show": show, "variant": variant, "search": search}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def settings(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SubscriptionsSettingsResult:
        """**Get subscription settings**

        What a buyer may do for themselves from their customer panel, when renewal reminders go, how long a past due one is kept, and whether an ended one's keys and files are taken back. `meta.plans` is the store's plans and `meta.limits` the ceilings each setting is held to.

        Needs the `subscriptions.read` permission (Read Subscriptions).

        Docs: https://docs.shoply.gg/api-reference/subscriptions/get-subscription-settings
        """
        return cast("SubscriptionsSettingsResult", self._caller._call("subscriptions.settings", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def updateSettings(
        self,
        *,
        cancelOn: Optional[bool] = None,
        cancelMode: Optional[Literal["end", "now"]] = None,
        undoOn: Optional[bool] = None,
        pauseOn: Optional[bool] = None,
        pauseDays: Optional[int] = None,
        pausesAYear: Optional[int] = None,
        remindersOn: Optional[bool] = None,
        reminderDays: Optional[List[int]] = None,
        graceDays: Optional[int] = None,
        revokeOn: Optional[bool] = None,
        autoOn: Optional[bool] = None,
        cardChangeOn: Optional[bool] = None,
        chargeTries: Optional[int] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SubscriptionsUpdateSettingsResult:
        """**Change subscription settings**

        Changes the settings named and keeps the rest. A change reaches every subscription from then on, the running ones included.

        Needs the `subscriptions.write` permission (Change Subscriptions).

        Args:
            cancelOn: Whether a buyer may cancel from their customer panel.
            cancelMode: When a buyer's cancellation takes effect: when what was paid for runs out, or straight away.
            undoOn: Whether a buyer may take a cancellation back before it takes effect.
            pauseOn: Whether a buyer may pause from their customer panel.
            pauseDays: The longest a buyer may pause for, from 1 to 365 days.
            pausesAYear: How many times in a year a buyer may pause, from 1 to 12.
            remindersOn: Whether the buyer is reminded before a renewal is due.
            reminderDays: How many days before it is due each reminder goes: up to 5, each from 1 to 30.
            graceDays: How long a renewal may go unpaid after the period runs out before the subscription ends, from 0 to 30 days.
            revokeOn: Whether an ended or paused subscription's keys and files are hidden from its buyer.
            autoOn: Whether a card paid with through Stripe, Authorize.net, Tagada, Mollie, MONEI, Adyen or Square, or through NMI where its Keep Cards for Subscriptions is on, is kept and each renewal charged to it by itself. Off, every renewal is paid by an emailed link.
            cardChangeOn: Whether a renewal a buyer pays by its link with another card keeps that card, and a buyer whose card is kept through Stripe may give another on Stripe's own page.
            chargeTries: How many times a declined card is tried, one a day while the grace days last, from 1 to 5.

        Docs: https://docs.shoply.gg/api-reference/subscriptions/change-subscription-settings
        """
        return cast("SubscriptionsUpdateSettingsResult", self._caller._call("subscriptions.updateSettings", [], {"cancelOn": cancelOn, "cancelMode": cancelMode, "undoOn": undoOn, "pauseOn": pauseOn, "pauseDays": pauseDays, "pausesAYear": pausesAYear, "remindersOn": remindersOn, "reminderDays": reminderDays, "graceDays": graceDays, "revokeOn": revokeOn, "autoOn": autoOn, "cardChangeOn": cardChangeOn, "chargeTries": chargeTries}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def plans(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[SubscriptionsPlansResultItem]:
        """**List subscription plans**

        Which of the store's options are sold as subscriptions, each with how often it renews and how many subscriptions to it are running. An option on this list is sold only as a subscription, and bought on its own.

        Needs the `subscriptions.read` permission (Read Subscriptions).

        Docs: https://docs.shoply.gg/api-reference/subscriptions/list-subscription-plans
        """
        return cast("List[SubscriptionsPlansResultItem]", self._caller._call("subscriptions.plans", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def savePlans(
        self,
        *,
        items: List[Dict[str, Any]],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[SubscriptionsSavePlansResultItem]:
        """**Sell options as subscriptions**

        Makes options subscriptions, or changes how often one renews. A change reaches new subscriptions only: a running one renews as it started. A store has as many subscription options as its plan does. The answer is every plan the store has.

        Needs the `subscriptions.write` permission (Change Subscriptions).

        Args:
            items: The options and how often each renews. Required.

        Docs: https://docs.shoply.gg/api-reference/subscriptions/sell-options-as-subscriptions
        """
        return cast("List[SubscriptionsSavePlansResultItem]", self._caller._call("subscriptions.savePlans", [], {"items": items}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def removePlan(
        self,
        variant_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Union[List[Any], Dict[str, Any]]:
        """**Sell an option once again**

        The option is sold once again from now on. Subscriptions already running to it go on renewing until they are cancelled. The answer is every plan left.

        Needs the `subscriptions.write` permission (Change Subscriptions).

        Docs: https://docs.shoply.gg/api-reference/subscriptions/sell-an-option-once-again
        """
        return cast("Union[List[Any], Dict[str, Any]]", self._caller._call("subscriptions.removePlan", [variant_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def show(
        self,
        subscription_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SubscriptionsShowResult:
        """**Get a subscription**

        The subscription as `data`, with `meta.history` (what happened to it, newest first) and `meta.orders` (its first order and every renewal). An order's `subscriptionId` names the subscription it started or renewed.

        Needs the `subscriptions.read` permission (Read Subscriptions).

        Docs: https://docs.shoply.gg/api-reference/subscriptions/get-a-subscription
        """
        return cast("SubscriptionsShowResult", self._caller._call("subscriptions.show", [subscription_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def cancel(
        self,
        subscription_id: str,
        *,
        when: Optional[Literal["end", "now"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SubscriptionsCancelResult:
        """**Cancel a subscription**

        At the end of what was paid for, or straight away. A past due or paused one ends straight away whichever is asked. A renewal waiting to be paid is cancelled. Whatever the store lets its buyers do, the store may always cancel. The subscription as `data`, with `meta.history` (what happened to it, newest first) and `meta.orders` (its first order and every renewal).

        Needs the `subscriptions.write` permission (Change Subscriptions).

        Args:
            when: When it ends. Left out, it is "end".

        Docs: https://docs.shoply.gg/api-reference/subscriptions/cancel-a-subscription
        """
        return cast("SubscriptionsCancelResult", self._caller._call("subscriptions.cancel", [subscription_id], {"when": when}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def undo(
        self,
        subscription_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SubscriptionsUndoResult:
        """**Undo a cancellation**

        Takes back a cancellation that has not taken effect yet, so it renews again. Refused with 409 for one that has ended, or whose option was deleted. The subscription as `data`, with `meta.history` (what happened to it, newest first) and `meta.orders` (its first order and every renewal).

        Needs the `subscriptions.write` permission (Change Subscriptions).

        Docs: https://docs.shoply.gg/api-reference/subscriptions/undo-a-cancellation
        """
        return cast("SubscriptionsUndoResult", self._caller._call("subscriptions.undo", [subscription_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def pause(
        self,
        subscription_id: str,
        *,
        days: int,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SubscriptionsPauseResult:
        """**Pause a subscription**

        Starts at once: nothing renews, a renewal waiting to be paid is cancelled, and where the store takes access back its keys and files are hidden until it resumes. The days left of what was paid for are kept: it renews that much later. It resumes by itself after `days`. The buyer is emailed. The subscription as `data`, with `meta.history` (what happened to it, newest first) and `meta.orders` (its first order and every renewal).

        Needs the `subscriptions.write` permission (Change Subscriptions).

        Args:
            days: How long, from 1 to 365 days. Required.

        Docs: https://docs.shoply.gg/api-reference/subscriptions/pause-a-subscription
        """
        return cast("SubscriptionsPauseResult", self._caller._call("subscriptions.pause", [subscription_id], {"days": days}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def resume(
        self,
        subscription_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SubscriptionsResumeResult:
        """**Resume a subscription**

        Ends a pause now, whoever paused it. Refused with 409 for one that is not paused. The subscription as `data`, with `meta.history` (what happened to it, newest first) and `meta.orders` (its first order and every renewal).

        Needs the `subscriptions.write` permission (Change Subscriptions).

        Docs: https://docs.shoply.gg/api-reference/subscriptions/resume-a-subscription
        """
        return cast("SubscriptionsResumeResult", self._caller._call("subscriptions.resume", [subscription_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def addDays(
        self,
        subscription_id: str,
        *,
        days: int,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SubscriptionsAddDaysResult:
        """**Add free days**

        Moves its next renewal later by that many days, at no charge, and every renewal after it with it. The subscription as `data`, with `meta.history` (what happened to it, newest first) and `meta.orders` (its first order and every renewal).

        Needs the `subscriptions.write` permission (Change Subscriptions).

        Args:
            days: How many, from 1 to 365. Required.

        Docs: https://docs.shoply.gg/api-reference/subscriptions/add-free-days
        """
        return cast("SubscriptionsAddDaysResult", self._caller._call("subscriptions.addDays", [subscription_id], {"days": days}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def email(
        self,
        subscription_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SubscriptionsEmailResult:
        """**Email the renewal again**

        Sends the buyer the link to pay their renewal again, for one whose renewal is waiting. Once an hour a subscription, and 20 every 10 minutes a store, whoever asks: after that the answer is 429. Refused with 409 where no renewal is waiting. The subscription as `data`, with `meta.history` (what happened to it, newest first) and `meta.orders` (its first order and every renewal).

        Needs the `subscriptions.write` permission (Change Subscriptions). It sends an email, and is counted against a budget of its own: 60 in ten minutes for each key.

        Docs: https://docs.shoply.gg/api-reference/subscriptions/email-the-renewal-again
        """
        return cast("SubscriptionsEmailResult", self._caller._call("subscriptions.email", [subscription_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Orders:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        page: Optional[int] = None,
        perPage: Optional[int] = None,
        status: Optional[Literal["pending", "completed", "refunded", "cancelled", "chargeback", "imported"]] = None,
        gateway: Optional[str] = None,
        search: Optional[str] = None,
        sort: Optional[Literal["created_at", "amount", "email", "status"]] = None,
        direction: Optional[Literal["asc", "desc"]] = None,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[OrdersListItem]:
        """**List orders**

        The store's orders, a page at a time, newest first unless sorted otherwise. `meta.statusCounts` says how many orders are in each status, and `meta.stats` what the orders matched come to.

        Needs the `orders.read` permission (Read Orders).

        Args:
            page: Which page of the list. The first is 1. Left out, it is 1.
            perPage: How many a page holds, up to 100. Left out, it is 20.
            status: Only orders in this status.
            gateway: Only orders paid with this payment method, by its name in the payment methods list.
            search: An order's ID, an imported order's ID on the platform it came from, or part of a buyer's email.
            sort: What the list is ordered by. Left out, it is "created_at".
            direction: Which way it is ordered. Left out, it is "desc".
            range: Only orders placed in this period.
            from_: Only orders placed on or after this day, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Only orders placed on or before this day, as `YYYY-MM-DD`.
            tz: The time zone the days of `range`, `from` and `to` are in, as an IANA name. Left out, UTC.

        Docs: https://docs.shoply.gg/api-reference/orders/list-orders
        """
        return cast("Page[OrdersListItem]", self._caller._call("orders.list", [], {"page": page, "perPage": perPage, "status": status, "gateway": gateway, "search": search, "sort": sort, "direction": direction, "range": range, "from": from_, "to": to, "tz": tz}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def export(
        self,
        *,
        status: Optional[Literal["pending", "completed", "refunded", "cancelled", "chargeback", "imported"]] = None,
        gateway: Optional[str] = None,
        search: Optional[str] = None,
        sort: Optional[Literal["created_at", "amount", "email", "status"]] = None,
        direction: Optional[Literal["asc", "desc"]] = None,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        rows: Optional[Literal["orders", "lines"]] = None,
        check: Optional[Literal["1"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> File:
        """**Export orders**

        The orders the same filters would list, as a CSV file: a row an order with every field its page shows (when it was paid, the fee, tax, balance and affiliate in it, the currency it was charged in, the billing address), or a row a product line with `rows=lines`. The first thirteen columns are always Order ID, Created, Email, Status, Payment, Currency, Subtotal, Discount, Total, Coupon, Country, Items and Products, in that order. No delivered key is in it. Every order the filters match is in the file, however many: it is sent as it is read, with no length given. Add `check=1` for `{ rows }`, how many it would have, which is not counted. A store exports at most 30 files every 10 minutes, orders, customers, fraud events and blacklist rules together, whoever asks: after that the answer is 429.

        Needs the `orders.read` permission (Read Orders). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Args:
            status: Only orders in this status.
            gateway: Only orders paid with this payment method, by its name in the payment methods list.
            search: An order's ID, an imported order's ID on the platform it came from, or part of a buyer's email.
            sort: What the list is ordered by. Left out, it is "created_at".
            direction: Which way it is ordered. Left out, it is "desc".
            range: Only orders placed in this period.
            from_: Only orders placed on or after this day, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Only orders placed on or before this day, as `YYYY-MM-DD`.
            tz: The time zone the days of `range`, `from` and `to` are in, as an IANA name. Left out, UTC.
            rows: What a row is: an order, or one product line of one. Left out, it is "orders".
            check: `1` for how many rows the file would have, as `{ rows }`, in place of the file. Not counted against the store's exports, and refused with 429 where none are left.

        Docs: https://docs.shoply.gg/api-reference/orders/export-orders
        """
        return cast("File", self._caller._call("orders.export", [], {"status": status, "gateway": gateway, "search": search, "sort": sort, "direction": direction, "range": range, "from": from_, "to": to, "tz": tz, "rows": rows, "check": check}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def show(
        self,
        order_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> OrdersShowResult:
        """**Get an order**

        One order with everything its page shows: its lines and what each delivered, its payments, the buyer, its timeline, where it came from, `refund`, which says which ways it can be refunded, and `requests`: what Shoply sent your servers about it, each try of each webhook about the order and each line's dynamic delivery, newest first, with the first 300 characters of what came back. `customPayment` is for an order paid with one of your custom payment methods, and null for any other: the method's name, `status` (`open`, `review` while it waits for you to approve or reject it, `paid` or `rejected`), the amount, and `proof`, what the buyer sent when they said they paid (the reference, whether a proof of payment was sent, and when). An order brought across by Platform Migration is found by its ID on the platform it came from as well, and answers with its own `id`; what it delivered there is in its items' `deliveredKeys`, a line of it each, where that platform says.

        Needs the `orders.read` permission (Read Orders).

        Docs: https://docs.shoply.gg/api-reference/orders/get-an-order
        """
        return cast("OrdersShowResult", self._caller._call("orders.show", [order_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def network(
        self,
        order_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Get an order's network**

        What is known about the connection the order was placed from: its provider, and whether it looks like a VPN, a proxy or a data centre. Asked of a lookup service when it is called, so it is a route of its own.

        Needs the `orders.read` permission (Read Orders). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Docs: https://docs.shoply.gg/api-reference/orders/get-an-orders-network
        """
        return cast("Any", self._caller._call("orders.network", [order_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def pdf(
        self,
        order_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> File:
        """**Get an order's PDF**

        The order's invoice as a PDF file. Every order has one, paid or not.

        Needs the `orders.read` permission (Read Orders). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Docs: https://docs.shoply.gg/api-reference/orders/get-an-orders-pdf
        """
        return cast("File", self._caller._call("orders.pdf", [order_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def markPaid(
        self,
        order_id: str,
        *,
        transactionId: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> OrdersMarkPaidResult:
        """**Mark an order as paid**

        Completes a pending or cancelled order as a payment would: it is delivered, its receipt is sent and it counts as revenue. For money that reached you some other way.

        Refused if any line cannot be delivered in full, so an order is never half delivered. Refused for an order that was refunded or charged back, and for a checkout the buyer never pressed Pay on, which has nobody to deliver to.

        Needs the `orders.fulfil` permission (Deliver Orders).

        Args:
            transactionId: Your own reference for the payment, up to 100 characters. Shown on the order.

        Docs: https://docs.shoply.gg/api-reference/orders/mark-an-order-as-paid
        """
        return cast("OrdersMarkPaidResult", self._caller._call("orders.markPaid", [order_id], {"transactionId": transactionId}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def refund(
        self,
        order_id: str,
        *,
        destination: Literal["source", "balance", "record"],
        reason: Literal["requested", "duplicate", "fraudulent", "other"],
        amount: Optional[float] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> OrdersRefundResult:
        """**Refund an order**

        Refunds a completed order, all of it. Which `destination` an order can take is in `refund` on the order: a payment method that cannot send money back (crypto, always) can only be refunded as store credit or recorded.

        Send an `Idempotency-Key` with this request. The order is marked refunded only once the payment provider has said the money is on its way, or the buyer has been credited.

        Needs the `orders.refund` permission (Refund Orders).

        Args:
            destination: `source`: back through the payment provider, to what paid. `balance`: credit on the buyer's balance at the store. `record`: only marked as refunded, because you returned the money yourself. Required.
            reason: Why. Required.
            amount: For `balance` only: how much to credit, from 0.01 up to what was paid, with at most 2 decimals. Left out, all of it.

        Docs: https://docs.shoply.gg/api-reference/orders/refund-an-order
        """
        return cast("OrdersRefundResult", self._caller._call("orders.refund", [order_id], {"destination": destination, "reason": reason, "amount": amount}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def redeliver(
        self,
        order_id: str,
        *,
        itemIds: Optional[List[int]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> OrdersRedeliverResult:
        """**Deliver an order again**

        Gives the buyer fresh license keys for the order's lines and emails them. The keys those lines held before are revoked, not returned to stock, so this costs stock: it is for a key that did not work.

        It goes to the order's own email address. Sending an order to another address is done in the dashboard.

        One order is delivered again at most ten times an hour, whoever asks: after that the answer is 429.

        Needs the `orders.fulfil` permission (Deliver Orders).

        Args:
            itemIds: The order's lines to act on, by their IDs. Left out, every line it applies to.

        Docs: https://docs.shoply.gg/api-reference/orders/deliver-an-order-again
        """
        return cast("OrdersRedeliverResult", self._caller._call("orders.redeliver", [order_id], {"itemIds": itemIds}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def retryDelivery(
        self,
        order_id: str,
        *,
        itemIds: Optional[List[int]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Retry a dynamic delivery**

        Asks your delivery endpoint again for the lines whose dynamic delivery failed. Nothing is revoked: those lines never delivered anything. A store may ask for 150 of these in ten minutes.

        Needs the `orders.fulfil` permission (Deliver Orders).

        Args:
            itemIds: The order's lines to act on, by their IDs. Left out, every line it applies to.

        Docs: https://docs.shoply.gg/api-reference/orders/retry-a-dynamic-delivery
        """
        return cast("Any", self._caller._call("orders.retryDelivery", [order_id], {"itemIds": itemIds}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def resendEmail(
        self,
        order_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Send an order's email again**

        Sends the order's delivery email again, with what it delivered, to the order's own email address. One customer's order emails are sent again at most five times an hour at your store, across all their orders and whoever asks: after that the answer is 429.

        Needs the `orders.fulfil` permission (Deliver Orders). It sends an email, and is counted against a budget of its own: 60 in ten minutes for each key.

        Docs: https://docs.shoply.gg/api-reference/orders/send-an-orders-email-again
        """
        return cast("Any", self._caller._call("orders.resendEmail", [order_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def approvePayment(
        self,
        order_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> OrdersApprovePaymentResult:
        """**Approve a payment to check**

        Approves the payment a buyer says they made with one of the store's custom payment methods, and completes the order as a payment would: its keys are delivered and its receipt sent. Only for an order whose payment waits for review (an `order.payment_submitted` webhook says so). Shoply never sees that money: approve once you have seen it arrive. Answers the order's ID, its `status`, and `dynamic`, what each dynamic delivery answered. One that cannot deliver (short of stock) is refused with why, and still waits.

        Needs the `orders.fulfil` permission (Deliver Orders).

        Docs: https://docs.shoply.gg/api-reference/orders/approve-a-payment-to-check
        """
        return cast("OrdersApprovePaymentResult", self._caller._call("orders.approvePayment", [order_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def rejectPayment(
        self,
        order_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> OrdersRejectPaymentResult:
        """**Reject a payment to check**

        Rejects the payment a buyer says they made with a custom method, and cancels the order. Its coupon's use is handed back, and the buyer is not emailed.

        Needs the `orders.fulfil` permission (Deliver Orders).

        Docs: https://docs.shoply.gg/api-reference/orders/reject-a-payment-to-check
        """
        return cast("OrdersRejectPaymentResult", self._caller._call("orders.rejectPayment", [order_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def proof(
        self,
        order_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Get an order's proof of payment**

        The picture a buyer sent with a payment made with a custom method, as the file itself: a PNG, JPEG or WebP. Under the permission that approves the payment, since it is what the payment is checked by. 404 where the order has none.

        Needs the `orders.fulfil` permission (Deliver Orders).

        Docs: https://docs.shoply.gg/api-reference/orders/get-an-orders-proof-of-payment
        """
        return cast("Any", self._caller._call("orders.proof", [order_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setNote(
        self,
        order_id: str,
        *,
        note: str,
        expectedNote: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> OrdersSetNoteResult:
        """**Write an order's note**

        Sets the store's own note on the order. The buyer never sees it.

        Needs the `orders.write` permission (Change Orders).

        Args:
            note: The note. Empty clears it. Required.
            expectedNote: The note as you last read it. Sent, the change is refused with `stale_write` if somebody has changed it since.

        Docs: https://docs.shoply.gg/api-reference/orders/write-an-orders-note
        """
        return cast("OrdersSetNoteResult", self._caller._call("orders.setNote", [order_id], {"note": note, "expectedNote": expectedNote}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Invoices:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        page: Optional[int] = None,
        perPage: Optional[int] = None,
        status: Optional[Literal["pending", "completed", "refunded", "cancelled", "chargeback"]] = None,
        search: Optional[str] = None,
        kind: Optional[Literal["invoice", "link"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[InvoicesListItem]:
        """**List invoices**

        The invoices the store has raised, a page at a time, newest first. An invoice is an order the store made for a buyer to pay: `orderId` is that order, and `payUrl` the page it is paid on. A payment link is listed with them (`kind` is `link`): an amount and what it is for (`title`), with no buyer on it (`email` is empty) until it is emailed to somebody or paid. One made in another currency than the store's says what the buyer is asked for in `charge`.

        Needs the `invoices.read` permission (Read Invoices).

        Args:
            page: Which page of the list. The first is 1. Left out, it is 1.
            perPage: How many a page holds, up to 100. Left out, it is 20.
            status: Only invoices whose order is in this status.
            search: An invoice's number, part of a buyer's email or name, or part of what a payment link is for.
            kind: Only invoices written for a buyer, or only payment links.

        Docs: https://docs.shoply.gg/api-reference/invoices/list-invoices
        """
        return cast("Page[InvoicesListItem]", self._caller._call("invoices.list", [], {"page": page, "perPage": perPage, "status": status, "search": search, "kind": kind}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        email: str,
        gateways: List[str],
        items: List[Dict[str, Any]],
        name: Optional[str] = None,
        note: Optional[str] = None,
        dueDays: Optional[int] = None,
        send: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Create an invoice**

        Raises an invoice: an order for a buyer to pay, with a page to pay it on. This is how a script makes an order. The answer has the order's ID (`orderId`) and the page it is paid on (`payUrl`), which you can hand to the buyer yourself.

        With `send` on, the invoice is also emailed to the buyer with its PDF. A store may email one invoice in five minutes, so a script that makes many leaves `send` off and delivers the link itself.

        A product line costs what the product costs. For any other price, add a line of your own with a `description` and a `unitPrice`. An invoice carries no automatic tax. A store may hold up to 2,000 unpaid invoices at once.

        Needs the `invoices.write` permission (Raise Invoices). It makes an order, and is counted against a budget of its own: 60 a minute for each key.

        Args:
            email: The buyer's email address. Required.
            gateways: The payment methods the buyer may pay with, by their names in the payment methods list. At least one the store has switched on. Required.
            items: What is being charged for, up to 50 lines. Each is a product from the catalogue (`productId`, `variantId`, `quantity`) or a line of your own (`description`, `quantity`, `unitPrice`). Required.
            name: The buyer's name, up to 120 characters. Printed on the invoice.
            note: A note printed on the invoice, up to 1,000 characters.
            dueDays: How many days the buyer has to pay: 1 to 30. Left out, it is 7.
            send: Whether to email the invoice to the buyer now. Left out, it is true.

        Docs: https://docs.shoply.gg/api-reference/invoices/create-an-invoice
        """
        return cast("Any", self._caller._call("invoices.create", [], {"email": email, "gateways": gateways, "items": items, "name": name, "note": note, "dueDays": dueDays, "send": send}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def send(
        self,
        order_id: str,
        *,
        email: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Send an invoice**

        Emails the invoice to the address on it, with its PDF. Only while it can still be paid, and one invoice email a store in five minutes.

        A payment link has no address on it until it is sent or paid, so the first send names one in `email`. The link is that buyer's from then on: the page it is paid on stops asking who is paying, and a later send with no `email` goes to the same address. It cannot be sent to another address once somebody has started paying it (`link_in_use`).

        A link that can be paid more than once stays nobody's: every send names an `email`, which is only where that one email goes, and it may be sent to as many people as you like at the same pace.

        Needs the `invoices.write` permission (Raise Invoices). It sends an email, and is counted against a budget of its own: 60 in ten minutes for each key.

        Args:
            email: For a payment link: the address to send it to. Left out, it goes to the address already on it.

        Docs: https://docs.shoply.gg/api-reference/invoices/send-an-invoice
        """
        return cast("Any", self._caller._call("invoices.send", [order_id], {"email": email}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def link(
        self,
        *,
        amount: Optional[float] = None,
        description: Optional[str] = None,
        currency: Optional[str] = None,
        uses: Optional[int] = None,
        items: Optional[List[Dict[str, Any]]] = None,
        gateways: Optional[List[str]] = None,
        expiresAt: Optional[str] = None,
        dueDays: Optional[int] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> InvoicesLinkResult:
        """**Create a payment link**

        Makes a payment link: an invoice for an amount, with no buyer on it. `payUrl` in the answer is the link. Whoever opens it gives their email address and pays, and the order is theirs. It is an invoice in every other way: it is listed with them, has a number and a PDF, and is cancelled if it is not paid in seven days.

        A link is paid once unless `uses` says more. A link for more than one payment is never the order that is paid: each person who presses Pay on it is given an order and an invoice of their own, which names the link in `linkOf`, and the link's `uses` says how many times it has been paid and how many are left. The count is asked when Pay is pressed, so two people who press it for the last use at the same moment can both pay.

        It may be paid with whichever payment methods the store has switched on when it is made. It counts toward the 2,000 unpaid invoices a store may hold at once. To email it to somebody, send it (Send an invoice) with their address.

        With `currency`, the amount is in that currency and the buyer is charged exactly it, where the store may charge in it: its own currency always, and the others only while adaptive pricing is on. The order is then for the amount's worth in the store's currency at the rate of the moment.

        With `items`, the link sells products in place of an amount: it is for what they cost, in the store's own currency, and whoever pays is sent them as any buyer is. `amount` and `description` are then left out. What it sells has to be in stock when the link is made, and again each time somebody pays through a link for several payments (`out_of_stock`).

        It may be paid with every payment method the store has switched on, or with the ones named in `gateways`. It is open for seven days, or until `expiresAt`, or for `dueDays` days, up to 365.

        Needs the `invoices.write` permission (Raise Invoices). It makes an order, and is counted against a budget of its own: 60 a minute for each key.

        Args:
            amount: How much to ask for, above zero. Left out when `items` is sent.
            description: What it is for, up to 255 characters. The buyer sees it as the order's one line. Left out, the line is called Payment.
            currency: The currency the amount is in and the buyer is charged in, as a three-letter code. Left out, the store's own.
            uses: How many times the link can be paid: 1 to 1,000. Left out, it is 1.
            items: Products the link sells, in place of an amount: up to 50 lines.
            gateways: The payment methods it may be paid with, by their names in the payment methods list. Left out, every method the store has switched on.
            expiresAt: When it stops being payable, as a date and time, or a day (`YYYY-MM-DD`) for the end of that day. At least an hour from now and at most 365 days.
            dueDays: In place of `expiresAt`: how many days it is open, 1 to 365. Left out, it is 7.

        Docs: https://docs.shoply.gg/api-reference/invoices/create-a-payment-link
        """
        return cast("InvoicesLinkResult", self._caller._call("invoices.link", [], {"amount": amount, "description": description, "currency": currency, "uses": uses, "items": items, "gateways": gateways, "expiresAt": expiresAt, "dueDays": dueDays}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def deleteLink(
        self,
        order_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Delete a payment link**

        Removes a payment link nobody has paid or started to pay. Its address stops working for anyone who has it.

        Only a payment link, never an invoice (`not_a_link`). Not one that was paid, which is an order (`link_paid`), and not one somebody has pressed Pay on, in case their payment arrives (`link_in_use`): that one closes by itself on its due day.

        Needs the `invoices.write` permission (Raise Invoices).

        Docs: https://docs.shoply.gg/api-reference/invoices/delete-a-payment-link
        """
        return cast("Any", self._caller._call("invoices.deleteLink", [order_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Reviews:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        page: Optional[int] = None,
        perPage: Optional[int] = None,
        rating: Optional[int] = None,
        type: Optional[Literal["buyer", "automatic"]] = None,
        search: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[ReviewsListItem]:
        """**List reviews**

        The reviews left on the store's orders, a page at a time, newest first. A buyer leaves one for a paid order; an order nobody reviewed is given five stars by itself after seven days. `meta.summary` is the whole store's average and counts, whatever the filters. A review the store flagged for removal carries `flag`: how it stands (`open`, or `kept` with the answer given) and why it was flagged. One that was removed is no longer listed.

        Needs the `reviews.read` permission (Read Reviews).

        Args:
            page: Which page of the list. The first is 1. Left out, it is 1.
            perPage: How many a page holds. Left out, it is 20.
            rating: Only reviews of this many stars: 1 to 5.
            type: Only reviews a buyer wrote, or only the ones given by themselves.
            search: A buyer's email, an order's ID, or words from a review.

        Docs: https://docs.shoply.gg/api-reference/reviews/list-reviews
        """
        return cast("Page[ReviewsListItem]", self._caller._call("reviews.list", [], {"page": page, "perPage": perPage, "rating": rating, "type": type, "search": search}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Coupons:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        page: Optional[int] = None,
        perPage: Optional[int] = None,
        search: Optional[str] = None,
        state: Optional[Literal["active", "inactive", "expired"]] = None,
        categoryId: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[CouponsListItem]:
        """**List coupons**

        The store's coupons, a page at a time, each with how often it has been used and what it has taken off. `meta.counts` says how many there are in each state.

        Needs the `coupons.read` permission (Read Coupons).

        Args:
            page: Which page of the list. The first is 1. Left out, it is 1.
            perPage: How many a page holds, up to 500. Left out, it is 20.
            search: Only coupons whose code contains this.
            state: Only coupons in this state.
            categoryId: Only coupons in this coupon category.

        Docs: https://docs.shoply.gg/api-reference/coupons/list-coupons
        """
        return cast("Page[CouponsListItem]", self._caller._call("coupons.list", [], {"page": page, "perPage": perPage, "search": search, "state": state, "categoryId": categoryId}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        code: str,
        value: float,
        tz: Optional[str] = None,
        discountType: Optional[Literal["percent", "fixed"]] = None,
        maxUses: Optional[int] = None,
        minSubtotal: Optional[float] = None,
        expiresAt: Optional[str] = None,
        active: Optional[bool] = None,
        categoryId: Optional[str] = None,
        appliesTo: Optional[Literal["all", "some"]] = None,
        targets: Optional[List[Dict[str, Any]]] = None,
        customerTag: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CouponsCreateResult:
        """**Create a coupon**

        Adds a coupon. Its expiry cannot already have passed.

        Needs the `coupons.write` permission (Change Coupons).

        Args:
            code: What a buyer types. 3 to 64 letters, digits, hyphens or underscores, kept in capitals. One coupon a code in a store. Required.
            value: How much comes off: 1 to 100 for `percent`, an amount for `fixed`. Required.
            tz: The time zone a bare date in `expiresAt` is read in, as an IANA name. Left out, UTC.
            discountType: A share of the order, or an amount in the store's currency. Left out, it is "percent".
            maxUses: How many orders may use it. 0 is no limit. Left out, it is 0.
            minSubtotal: The smallest order it works on, before discounts. 0 is any order. Left out, it is 0.
            expiresAt: When it stops working: a date (`2026-12-31`, good to the end of that day) or a date and time. Empty is never.
            active: Whether buyers can use it. Left out, it is true.
            categoryId: The coupon category it is filed in. Left out, it goes in the store's Default category.
            appliesTo: Every product, or only the ones in `targets`. Left out, it is "all".
            targets: The products it works on when `appliesTo` is `some`. Each names a product, and optionally one variant of it.
            customerTag: Who may use it: empty for anybody with the code, `vip`, or the ID of one of the store's tags. The buyer's email has to wear the tag when the code is applied and when they pay.

        Docs: https://docs.shoply.gg/api-reference/coupons/create-a-coupon
        """
        return cast("CouponsCreateResult", self._caller._call("coupons.create", [], {"code": code, "value": value, "tz": tz, "discountType": discountType, "maxUses": maxUses, "minSubtotal": minSubtotal, "expiresAt": expiresAt, "active": active, "categoryId": categoryId, "appliesTo": appliesTo, "targets": targets, "customerTag": customerTag}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        coupon_id: str,
        *,
        code: str,
        value: float,
        tz: Optional[str] = None,
        discountType: Optional[Literal["percent", "fixed"]] = None,
        maxUses: Optional[int] = None,
        minSubtotal: Optional[float] = None,
        expiresAt: Optional[str] = None,
        active: Optional[bool] = None,
        categoryId: Optional[str] = None,
        appliesTo: Optional[Literal["all", "some"]] = None,
        targets: Optional[List[Dict[str, Any]]] = None,
        customerTag: Optional[str] = None,
        expectedUpdatedAt: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CouponsUpdateResult:
        """**Update a coupon**

        Saves the coupon whole: send every field as it should be, not only what changed. A field left out goes back to its default. The exceptions are `appliesTo` and `targets`, which stay as they are when `appliesTo` is left out, and `customerTag`, which stays as it is when left out.

        Needs the `coupons.write` permission (Change Coupons).

        Args:
            code: What a buyer types. 3 to 64 letters, digits, hyphens or underscores, kept in capitals. One coupon a code in a store. Required.
            value: How much comes off: 1 to 100 for `percent`, an amount for `fixed`. Required.
            tz: The time zone a bare date in `expiresAt` is read in, as an IANA name. Left out, UTC.
            discountType: A share of the order, or an amount in the store's currency. Left out, it is "percent".
            maxUses: How many orders may use it. 0 is no limit. Left out, it is 0.
            minSubtotal: The smallest order it works on, before discounts. 0 is any order. Left out, it is 0.
            expiresAt: When it stops working: a date (`2026-12-31`, good to the end of that day) or a date and time. Empty is never.
            active: Whether buyers can use it. Left out, it is true.
            categoryId: The coupon category it is filed in. Left out, it goes in the store's Default category.
            appliesTo: Every product, or only the ones in `targets`. Left out, it is "all".
            targets: The products it works on when `appliesTo` is `some`. Each names a product, and optionally one variant of it.
            customerTag: Who may use it: empty for anybody with the code, `vip`, or the ID of one of the store's tags. The buyer's email has to wear the tag when the code is applied and when they pay.
            expectedUpdatedAt: The `updatedAt` you last read. Sent, the change is refused with `stale_write` if the record has changed since. Left out, it is saved whatever happened in between.

        Docs: https://docs.shoply.gg/api-reference/coupons/update-a-coupon
        """
        return cast("CouponsUpdateResult", self._caller._call("coupons.update", [coupon_id], {"code": code, "value": value, "tz": tz, "discountType": discountType, "maxUses": maxUses, "minSubtotal": minSubtotal, "expiresAt": expiresAt, "active": active, "categoryId": categoryId, "appliesTo": appliesTo, "targets": targets, "customerTag": customerTag, "expectedUpdatedAt": expectedUpdatedAt}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        coupon_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CouponsDeleteResult:
        """**Delete a coupon**

        Removes the coupon. Orders that used it keep the code they were placed with.

        Needs the `coupons.write` permission (Change Coupons).

        Docs: https://docs.shoply.gg/api-reference/coupons/delete-a-coupon
        """
        return cast("CouponsDeleteResult", self._caller._call("coupons.delete", [coupon_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def sort(
        self,
        *,
        couponIds: List[str],
        categoryId: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CouponsSortResult:
        """**Sort coupons**

        Sets the order of the coupons in one coupon category. Send every coupon of that category, in the order they should be in.

        Needs the `coupons.write` permission (Change Coupons).

        Args:
            couponIds: The coupons' IDs in their new order. Required.
            categoryId: The coupon category being sorted. Left out, the Default category.

        Docs: https://docs.shoply.gg/api-reference/coupons/sort-coupons
        """
        return cast("CouponsSortResult", self._caller._call("coupons.sort", [], {"couponIds": couponIds, "categoryId": categoryId}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class CouponCategories:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CouponCategoriesListResultItem]:
        """**List coupon categories**

        The categories the store files its coupons in, in the store's own order, each with how many coupons it holds. Two are the store's from the start and cannot be renamed or deleted: Default, and First Timer, which holds the codes the first-order reward makes.

        Needs the `coupons.read` permission (Read Coupons).

        Docs: https://docs.shoply.gg/api-reference/coupon-categories/list-coupon-categories
        """
        return cast("List[CouponCategoriesListResultItem]", self._caller._call("couponCategories.list", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        name: str,
        description: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CouponCategoriesCreateResult:
        """**Create a coupon category**

        Adds a category to file coupons in. A store holds up to 30 of its own.

        Needs the `coupons.write` permission (Change Coupons).

        Args:
            name: Its name. One category a name in a store. Required.
            description: A note for whoever manages the store. Buyers never see it.

        Docs: https://docs.shoply.gg/api-reference/coupon-categories/create-a-coupon-category
        """
        return cast("CouponCategoriesCreateResult", self._caller._call("couponCategories.create", [], {"name": name, "description": description}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        category_id: str,
        *,
        name: str,
        description: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CouponCategoriesUpdateResult:
        """**Update a coupon category**

        Renames a category or changes its note. The two the store starts with are refused with `system_category`.

        Needs the `coupons.write` permission (Change Coupons).

        Args:
            name: Its name. Required.
            description: A note for whoever manages the store.

        Docs: https://docs.shoply.gg/api-reference/coupon-categories/update-a-coupon-category
        """
        return cast("CouponCategoriesUpdateResult", self._caller._call("couponCategories.update", [category_id], {"name": name, "description": description}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        category_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CouponCategoriesDeleteResult:
        """**Delete a coupon category**

        Removes the category. The coupons in it are not deleted: they move to Default, since buyers may be holding their codes.

        Needs the `coupons.write` permission (Change Coupons).

        Docs: https://docs.shoply.gg/api-reference/coupon-categories/delete-a-coupon-category
        """
        return cast("CouponCategoriesDeleteResult", self._caller._call("couponCategories.delete", [category_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def sort(
        self,
        *,
        categoryIds: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Sort coupon categories**

        Sets the order the categories are listed in.

        Needs the `coupons.write` permission (Change Coupons).

        Args:
            categoryIds: The categories' IDs in their new order. Required.

        Docs: https://docs.shoply.gg/api-reference/coupon-categories/sort-coupon-categories
        """
        return cast("Any", self._caller._call("couponCategories.sort", [], {"categoryIds": categoryIds}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class CouponPopup:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def show(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CouponPopupShowResult:
        """**Get the coupon pop-up**

        The pop-up that offers visitors of the storefront a coupon. A store that never set one up reads back the defaults, switched off. `unusable` says why buyers are not being shown it when its coupon no longer works.

        Needs the `coupons.read` permission (Read Coupons).

        Docs: https://docs.shoply.gg/api-reference/coupon-pop-up/get-the-coupon-pop-up
        """
        return cast("CouponPopupShowResult", self._caller._call("couponPopup.show", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        *,
        enabled: Optional[bool] = None,
        couponId: Optional[str] = None,
        title: Optional[str] = None,
        message: Optional[str] = None,
        buttonText: Optional[str] = None,
        opens: Optional[Literal["delay", "leave"]] = None,
        delaySeconds: Optional[int] = None,
        frequency: Optional[Literal["page", "visit", "browser"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CouponPopupUpdateResult:
        """**Update the coupon pop-up**

        Saves the pop-up whole. Switched off, it is saved as it is, finished or not. Switched on, it needs a title and a coupon buyers can use today.

        Needs the `coupons.write` permission (Change Coupons).

        Args:
            enabled: Whether the storefront shows it. Left out, it is false.
            couponId: The coupon it hands out.
            title: Its heading, up to 80 characters.
            message: The line under the heading, up to 240 characters.
            buttonText: What its button says, up to 30 characters.
            opens: After a wait, or when the visitor looks like leaving. Left out, it is "delay".
            delaySeconds: How long the wait is when `opens` is `delay`: 0 to 120 seconds. Left out, it is 5.
            frequency: How often one visitor sees it: on every page, once a visit, or once in that browser. Left out, it is "visit".

        Docs: https://docs.shoply.gg/api-reference/coupon-pop-up/update-the-coupon-pop-up
        """
        return cast("CouponPopupUpdateResult", self._caller._call("couponPopup.update", [], {"enabled": enabled, "couponId": couponId, "title": title, "message": message, "buttonText": buttonText, "opens": opens, "delaySeconds": delaySeconds, "frequency": frequency}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Sales:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[SalesListResultItem]:
        """**List sales**

        Every sale the store has, newest first. A store holds as many as its plan does, 150 at most, so the list is not paged.

        Needs the `sales.read` permission (Read Sales).

        Docs: https://docs.shoply.gg/api-reference/sales/list-sales
        """
        return cast("List[SalesListResultItem]", self._caller._call("sales.list", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        name: str,
        value: float,
        startsAt: str,
        endsAt: str,
        tz: Optional[str] = None,
        discountType: Optional[Literal["percent", "fixed"]] = None,
        appliesTo: Optional[Literal["all", "some"]] = None,
        targets: Optional[List[Dict[str, Any]]] = None,
        couponRule: Optional[Literal["rest", "all", "none"]] = None,
        exceptions: Optional[List[Dict[str, Any]]] = None,
        enabled: Optional[bool] = None,
        showBar: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SalesCreateResult:
        """**Create a sale**

        Adds a sale. A store holds as many as its plan does.

        Needs the `sales.write` permission (Change Sales).

        Args:
            name: What the sale is called, up to 60 characters. Buyers see it on the storefront's countdown. Required.
            value: How much comes off: above 0 and up to 100 for `percent`, an amount with at most 2 decimals for `fixed`. Required.
            startsAt: When it starts, as a date and time. Required.
            endsAt: When it ends, as a date and time. After `startsAt`, and not already past. Required.
            tz: The time zone `startsAt` and `endsAt` are read in when they name none, as an IANA name. Left out, UTC.
            discountType: A share of each price, or an amount in the store's currency. Left out, it is "percent".
            appliesTo: Every product, or only the ones in `targets`. Left out, it is "all".
            targets: The products on sale when `appliesTo` is `some`. Each names a product, and optionally one variant of it.
            couponRule: What coupons do while the sale runs. `rest`: a coupon counts only the items in the cart that are not on sale. `all`: coupons work on sale items too. `none`: no coupon works anywhere in the store. Left out, it is "rest".
            exceptions: Up to 100 coupons or coupon categories that `couponRule` is turned around for.
            enabled: Whether the sale runs when its time comes. Left out, it is true.
            showBar: Whether the storefront shows the sale's countdown bar. Left out, it is true.

        Docs: https://docs.shoply.gg/api-reference/sales/create-a-sale
        """
        return cast("SalesCreateResult", self._caller._call("sales.create", [], {"name": name, "value": value, "startsAt": startsAt, "endsAt": endsAt, "tz": tz, "discountType": discountType, "appliesTo": appliesTo, "targets": targets, "couponRule": couponRule, "exceptions": exceptions, "enabled": enabled, "showBar": showBar}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def show(
        self,
        sale_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SalesShowResult:
        """**Get a sale**

        One sale, with the products it covers and its coupon exceptions.

        Needs the `sales.read` permission (Read Sales).

        Docs: https://docs.shoply.gg/api-reference/sales/get-a-sale
        """
        return cast("SalesShowResult", self._caller._call("sales.show", [sale_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        sale_id: str,
        *,
        name: str,
        value: float,
        startsAt: str,
        endsAt: str,
        tz: Optional[str] = None,
        discountType: Optional[Literal["percent", "fixed"]] = None,
        appliesTo: Optional[Literal["all", "some"]] = None,
        targets: Optional[List[Dict[str, Any]]] = None,
        couponRule: Optional[Literal["rest", "all", "none"]] = None,
        exceptions: Optional[List[Dict[str, Any]]] = None,
        enabled: Optional[bool] = None,
        showBar: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Update a sale**

        Saves the sale whole: send every field as it should be, not only what changed.

        Needs the `sales.write` permission (Change Sales).

        Args:
            name: What the sale is called, up to 60 characters. Buyers see it on the storefront's countdown. Required.
            value: How much comes off: above 0 and up to 100 for `percent`, an amount with at most 2 decimals for `fixed`. Required.
            startsAt: When it starts, as a date and time. Required.
            endsAt: When it ends, as a date and time. After `startsAt`, and not already past. Required.
            tz: The time zone `startsAt` and `endsAt` are read in when they name none, as an IANA name. Left out, UTC.
            discountType: A share of each price, or an amount in the store's currency. Left out, it is "percent".
            appliesTo: Every product, or only the ones in `targets`. Left out, it is "all".
            targets: The products on sale when `appliesTo` is `some`. Each names a product, and optionally one variant of it.
            couponRule: What coupons do while the sale runs. `rest`: a coupon counts only the items in the cart that are not on sale. `all`: coupons work on sale items too. `none`: no coupon works anywhere in the store. Left out, it is "rest".
            exceptions: Up to 100 coupons or coupon categories that `couponRule` is turned around for.
            enabled: Whether the sale runs when its time comes. Left out, it is true.
            showBar: Whether the storefront shows the sale's countdown bar. Left out, it is true.

        Docs: https://docs.shoply.gg/api-reference/sales/update-a-sale
        """
        return cast("Any", self._caller._call("sales.update", [sale_id], {"name": name, "value": value, "startsAt": startsAt, "endsAt": endsAt, "tz": tz, "discountType": discountType, "appliesTo": appliesTo, "targets": targets, "couponRule": couponRule, "exceptions": exceptions, "enabled": enabled, "showBar": showBar}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        sale_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SalesDeleteResult:
        """**Delete a sale**

        Removes the sale. Orders placed during it keep the prices they were charged.

        Needs the `sales.write` permission (Change Sales).

        Docs: https://docs.shoply.gg/api-reference/sales/delete-a-sale
        """
        return cast("SalesDeleteResult", self._caller._call("sales.delete", [sale_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setEnabled(
        self,
        sale_id: str,
        *,
        enabled: bool,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SalesSetEnabledResult:
        """**Switch a sale on or off**

        Changes whether the sale runs, without sending the rest of it.

        Needs the `sales.write` permission (Change Sales).

        Args:
            enabled: Whether the sale runs when its time comes. Required.

        Docs: https://docs.shoply.gg/api-reference/sales/switch-a-sale-on-or-off
        """
        return cast("SalesSetEnabledResult", self._caller._call("sales.setEnabled", [sale_id], {"enabled": enabled}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Blog:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[BlogListResultItem]:
        """**List blog categories and posts**

        Every blog category in the store's own order, each with its posts in theirs, drafts included, without their text. A store holds up to 20 categories and a category up to 15 posts.

        Needs the `blog.read` permission (Read Blog).

        Docs: https://docs.shoply.gg/api-reference/blog/list-blog-categories-and-posts
        """
        return cast("List[BlogListResultItem]", self._caller._call("blog.list", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class BlogCategories:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def create(
        self,
        *,
        name: str,
        description: Optional[str] = None,
        slug: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> BlogCategoriesCreateResult:
        """**Create a blog category**

        Adds a category for posts to go in. A category with no published post is nowhere on the store.

        Needs the `blog.write` permission (Change Blog).

        Args:
            name: The category's name. Required.
            description: What it is about. Shown on the blog's own page.
            slug: The part of its address after `/blog/`. Left out, it is made from the name. A post and a category cannot share one.

        Docs: https://docs.shoply.gg/api-reference/blog/create-a-blog-category
        """
        return cast("BlogCategoriesCreateResult", self._caller._call("blogCategories.create", [], {"name": name, "description": description, "slug": slug}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        category_id: str,
        *,
        name: str,
        description: Optional[str] = None,
        slug: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> BlogCategoriesUpdateResult:
        """**Update a blog category**

        Saves the category's name, description and address. A changed address is safe: the old one leads to the new.

        Needs the `blog.write` permission (Change Blog).

        Args:
            name: The category's name. Required.
            description: What it is about. Shown on the blog's own page.
            slug: The part of its address after `/blog/`. Left out, it is made from the name. A post and a category cannot share one.

        Docs: https://docs.shoply.gg/api-reference/blog/update-a-blog-category
        """
        return cast("BlogCategoriesUpdateResult", self._caller._call("blogCategories.update", [category_id], {"name": name, "description": description, "slug": slug}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        category_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> BlogCategoriesDeleteResult:
        """**Delete a blog category**

        Removes a category that has no posts. One that still has posts is refused with `blog_category_not_empty`: move or delete them first.

        Needs the `blog.write` permission (Change Blog).

        Docs: https://docs.shoply.gg/api-reference/blog/delete-a-blog-category
        """
        return cast("BlogCategoriesDeleteResult", self._caller._call("blogCategories.delete", [category_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def sort(
        self,
        *,
        ids: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> BlogCategoriesSortResult:
        """**Sort blog categories**

        Sets the order the blog's own page lists its categories in.

        Needs the `blog.write` permission (Change Blog).

        Args:
            ids: The categories' IDs in their new order. Required.

        Docs: https://docs.shoply.gg/api-reference/blog/sort-blog-categories
        """
        return cast("BlogCategoriesSortResult", self._caller._call("blogCategories.sort", [], {"ids": ids}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def uploadImage(
        self,
        category_id: str,
        *,
        file: Union[str, "os.PathLike[str]", bytes, BinaryIO],
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Upload a blog category's picture**

        Gives the category its one picture, replacing any it had. Sent as `multipart/form-data` in a field called `image`.

        Needs the `blog.write` permission (Change Blog).

        Args:
            file: A path on disk, the file's bytes, or a file opened for reading.
            filename: Its name. Left out, the path's own, or "upload".
            content_type: Its type, "image/png". Left out, worked out from the name.

        Docs: https://docs.shoply.gg/api-reference/blog/upload-a-blog-categorys-picture
        """
        return cast("Any", self._caller._call("blogCategories.uploadImage", [category_id], {"file": file, "filename": filename, "content_type": content_type}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def deleteImage(
        self,
        category_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Delete a blog category's picture**

        Removes the category's picture.

        Needs the `blog.write` permission (Change Blog).

        Docs: https://docs.shoply.gg/api-reference/blog/delete-a-blog-categorys-picture
        """
        return cast("Any", self._caller._call("blogCategories.deleteImage", [category_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class BlogPosts:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def create(
        self,
        *,
        categoryId: str,
        title: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> BlogPostsCreateResult:
        """**Create a blog post**

        Starts a post as a draft with a title and nothing else. Write it and publish it with "Update a blog post".

        Needs the `blog.write` permission (Change Blog).

        Args:
            categoryId: The blog category it goes in. Required.
            title: Its title.

        Docs: https://docs.shoply.gg/api-reference/blog/create-a-blog-post
        """
        return cast("BlogPostsCreateResult", self._caller._call("blogPosts.create", [], {"categoryId": categoryId, "title": title}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def show(
        self,
        post_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> BlogPostsShowResult:
        """**Get a blog post**

        One post with its text, as Markdown.

        Needs the `blog.read` permission (Read Blog).

        Docs: https://docs.shoply.gg/api-reference/blog/get-a-blog-post
        """
        return cast("BlogPostsShowResult", self._caller._call("blogPosts.show", [post_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        post_id: str,
        *,
        title: str,
        slug: Optional[str] = None,
        body: Optional[str] = None,
        status: Optional[Literal["draft", "published"]] = None,
        categoryId: Optional[str] = None,
        coverAlt: Optional[str] = None,
        seoTitle: Optional[str] = None,
        seoDescription: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> BlogPostsUpdateResult:
        """**Update a blog post**

        Saves the post whole: send every field as it should be. `status` and `categoryId` are the exceptions, and stay as they are when left out. The text is Markdown and nothing in it is trusted as HTML. A picture in the text that the text no longer shows is removed when the post is saved.

        Needs the `blog.write` permission (Change Blog).

        Args:
            title: Its title. Required.
            slug: The last part of its address. Left out, it is made from the title.
            body: The post's text, as Markdown.
            status: A draft is nowhere on the store. A published post is.
            categoryId: The blog category it is in. A post moved to another category is counted there as a new one.
            coverAlt: What its cover picture shows, for readers who cannot see it.
            seoTitle: Its own title in search results. Empty is its title.
            seoDescription: Its own description in search results. Empty is the start of its text.

        Docs: https://docs.shoply.gg/api-reference/blog/update-a-blog-post
        """
        return cast("BlogPostsUpdateResult", self._caller._call("blogPosts.update", [post_id], {"title": title, "slug": slug, "body": body, "status": status, "categoryId": categoryId, "coverAlt": coverAlt, "seoTitle": seoTitle, "seoDescription": seoDescription}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        post_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> BlogPostsDeleteResult:
        """**Delete a blog post**

        Removes the post and its pictures.

        Needs the `blog.write` permission (Change Blog).

        Docs: https://docs.shoply.gg/api-reference/blog/delete-a-blog-post
        """
        return cast("BlogPostsDeleteResult", self._caller._call("blogPosts.delete", [post_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setStatus(
        self,
        post_id: str,
        *,
        status: Literal["draft", "published"],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> BlogPostsSetStatusResult:
        """**Publish or unpublish a blog post**

        Puts a post out, or takes it back to a draft, and changes nothing else about it.

        Needs the `blog.write` permission (Change Blog).

        Args:
            status: The new status. Required.

        Docs: https://docs.shoply.gg/api-reference/blog/publish-or-unpublish-a-blog-post
        """
        return cast("BlogPostsSetStatusResult", self._caller._call("blogPosts.setStatus", [post_id], {"status": status}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def sort(
        self,
        *,
        categoryId: str,
        ids: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> BlogPostsSortResult:
        """**Sort a category's blog posts**

        Sets the order one category's page lists its posts in.

        Needs the `blog.write` permission (Change Blog).

        Args:
            categoryId: The blog category being sorted. Required.
            ids: The posts' IDs in their new order. Required.

        Docs: https://docs.shoply.gg/api-reference/blog/sort-a-categorys-blog-posts
        """
        return cast("BlogPostsSortResult", self._caller._call("blogPosts.sort", [], {"categoryId": categoryId, "ids": ids}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def uploadCover(
        self,
        post_id: str,
        *,
        file: Union[str, "os.PathLike[str]", bytes, BinaryIO],
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Upload a blog post's cover**

        Gives the post its one cover picture, replacing any it had. Sent as `multipart/form-data` in a field called `image`.

        Needs the `blog.write` permission (Change Blog).

        Args:
            file: A path on disk, the file's bytes, or a file opened for reading.
            filename: Its name. Left out, the path's own, or "upload".
            content_type: Its type, "image/png". Left out, worked out from the name.

        Docs: https://docs.shoply.gg/api-reference/blog/upload-a-blog-posts-cover
        """
        return cast("Any", self._caller._call("blogPosts.uploadCover", [post_id], {"file": file, "filename": filename, "content_type": content_type}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def deleteCover(
        self,
        post_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Delete a blog post's cover**

        Removes the post's cover picture.

        Needs the `blog.write` permission (Change Blog).

        Docs: https://docs.shoply.gg/api-reference/blog/delete-a-blog-posts-cover
        """
        return cast("Any", self._caller._call("blogPosts.deleteCover", [post_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def uploadImage(
        self,
        post_id: str,
        *,
        file: Union[str, "os.PathLike[str]", bytes, BinaryIO],
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Upload a picture for a blog post's text**

        Uploads a picture to use in the post's text, and answers its address (`url`) to write into the Markdown. Sent as `multipart/form-data` in a field called `image`. It stays the post's for as long as the saved text shows it.

        Needs the `blog.write` permission (Change Blog).

        Args:
            file: A path on disk, the file's bytes, or a file opened for reading.
            filename: Its name. Left out, the path's own, or "upload".
            content_type: Its type, "image/png". Left out, worked out from the name.

        Docs: https://docs.shoply.gg/api-reference/blog/upload-a-picture-for-a-blog-posts-text
        """
        return cast("Any", self._caller._call("blogPosts.uploadImage", [post_id], {"file": file, "filename": filename, "content_type": content_type}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Seo:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def show(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SeoShowResult:
        """**Get search settings**

        The four things a store sets once for search: its site verification codes, whether AI crawlers are asked to stay away, whether search engines are told of changes, and where paid orders are sent in Google Analytics.

        Needs the `seo.read` permission (Read Search Settings).

        Docs: https://docs.shoply.gg/api-reference/search-settings/get-search-settings
        """
        return cast("SeoShowResult", self._caller._call("seo.show", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        *,
        googleVerification: Optional[str] = None,
        bingVerification: Optional[str] = None,
        aiCrawlers: Optional[bool] = None,
        indexNow: Optional[bool] = None,
        measurementId: Optional[str] = None,
        apiSecret: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SeoUpdateResult:
        """**Update search settings**

        Changes the store's search settings. Only what is sent changes.

        Needs the `seo.write` permission (Change Search Settings).

        Args:
            googleVerification: The code Google Search Console gives a site's owner, as the code or as the whole meta tag. Empty removes it.
            bingVerification: The same, from Bing Webmaster Tools.
            aiCrawlers: Whether AI crawlers may read the store. Off, the store's robots.txt asks each of them not to.
            indexNow: Whether search engines are told when a product, a post or a page changes.
            measurementId: The Google Analytics property paid orders are sent to, as `G-XXXXXXXXXX`. Empty stops sending them.
            apiSecret: That property's Measurement Protocol API secret. It is never answered back.

        Docs: https://docs.shoply.gg/api-reference/search-settings/update-search-settings
        """
        return cast("SeoUpdateResult", self._caller._call("seo.update", [], {"googleVerification": googleVerification, "bingVerification": bingVerification, "aiCrawlers": aiCrawlers, "indexNow": indexNow, "measurementId": measurementId, "apiSecret": apiSecret}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Redirects:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[RedirectsListResultItem]:
        """**List redirects and broken links**

        The store's redirects, and under `meta.missing` the addresses people asked the store for that had nothing at them, most asked for first. A redirect from an address that still has a page is kept and waits: `live` says which.

        Needs the `seo.read` permission (Read Search Settings).

        Docs: https://docs.shoply.gg/api-reference/redirects/list-redirects-and-broken-links
        """
        return cast("List[RedirectsListResultItem]", self._caller._call("redirects.list", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        from_: str,
        to: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[RedirectsCreateResultItem]:
        """**Create a redirect**

        Sends an address that has nothing at it to one that has. It is followed only once the first address has turned out to be nothing, so a redirect can never take a page away. Adding one for a broken link takes that link off the list. Answers the store's redirects as they now stand.

        Needs the `seo.write` permission (Change Search Settings).

        Args:
            from_: The address that has nothing at it, as a path on the store (`/old-page`). A whole address of the store is cut down to its path. Required.
            to: Where it leads, as a path on the store. A redirect never leaves the store, and never leads to an address that is itself redirected. Required.

        Docs: https://docs.shoply.gg/api-reference/redirects/create-a-redirect
        """
        return cast("List[RedirectsCreateResultItem]", self._caller._call("redirects.create", [], {"from": from_, "to": to}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        redirect_id: str,
        *,
        from_: str,
        to: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[RedirectsUpdateResultItem]:
        """**Update a redirect**

        Changes where a redirect is from and where it leads. Answers the store's redirects as they now stand.

        Needs the `seo.write` permission (Change Search Settings).

        Args:
            from_: The address that has nothing at it, as a path on the store (`/old-page`). A whole address of the store is cut down to its path. Required.
            to: Where it leads, as a path on the store. A redirect never leaves the store, and never leads to an address that is itself redirected. Required.

        Docs: https://docs.shoply.gg/api-reference/redirects/update-a-redirect
        """
        return cast("List[RedirectsUpdateResultItem]", self._caller._call("redirects.update", [redirect_id], {"from": from_, "to": to}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        redirect_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Union[List[Any], Dict[str, Any]]:
        """**Delete a redirect**

        Removes a redirect. Answers the redirects that are left.

        Needs the `seo.write` permission (Change Search Settings).

        Docs: https://docs.shoply.gg/api-reference/redirects/delete-a-redirect
        """
        return cast("Union[List[Any], Dict[str, Any]]", self._caller._call("redirects.delete", [redirect_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class BrokenLinks:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def dismiss(
        self,
        *,
        path: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Union[List[Any], Dict[str, Any]]:
        """**Dismiss broken links**

        Takes one address off the list of broken links, or all of them when none is named. An address somebody asks for again is counted again.

        Needs the `seo.write` permission (Change Search Settings).

        Args:
            path: The one address to take off the list. Left out, the whole list is emptied.

        Docs: https://docs.shoply.gg/api-reference/redirects/dismiss-broken-links
        """
        return cast("Union[List[Any], Dict[str, Any]]", self._caller._call("brokenLinks.dismiss", [], {"path": path}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Sitemap:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def show(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SitemapShowResult:
        """**Get the sitemap**

        Every address the store has, a kind at a time (pages, categories, products, blog), each with whether the sitemap lists it, its priority and how often it is said to change. This is the file the store serves at `/sitemap.xml`.

        Needs the `seo.read` permission (Read Search Settings).

        Docs: https://docs.shoply.gg/api-reference/sitemap/get-the-sitemap
        """
        return cast("SitemapShowResult", self._caller._call("sitemap.show", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def updateKind(
        self,
        kind: str,
        *,
        listed: Optional[bool] = None,
        priority: Optional[str] = None,
        changefreq: Optional[Literal["always", "hourly", "daily", "weekly", "monthly", "yearly", "never"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SitemapUpdateKindResult:
        """**Update a kind of address**

        Sets the rule for a whole kind. Every address of that kind that has no rule of its own follows it, and a kind that is not listed lists none of its addresses. Send any of the three. Answers the whole sitemap again.

        Needs the `seo.write` permission (Change Search Settings).

        Args:
            listed: Whether the sitemap lists it.
            priority: Its priority, from `0.1` to `1.0`.
            changefreq: How often it changes.

        Docs: https://docs.shoply.gg/api-reference/sitemap/update-a-kind-of-address
        """
        return cast("SitemapUpdateKindResult", self._caller._call("sitemap.updateKind", [kind], {"listed": listed, "priority": priority, "changefreq": changefreq}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def updateEntry(
        self,
        *,
        kind: Literal["pages", "categories", "products", "blog"],
        ref: str,
        listed: Optional[bool] = None,
        priority: Optional[str] = None,
        changefreq: Optional[Literal["always", "hourly", "daily", "weekly", "monthly", "yearly", "never"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Update one address**

        Sets one address's own rule. An address set to what its kind says follows its kind again. Only an address the store has can be given a rule. Answers the whole sitemap again.

        Needs the `seo.write` permission (Change Search Settings).

        Args:
            kind: The kind the address is of. Required.
            ref: Which address of that kind, as "Get the sitemap" names it. Required.
            listed: Whether the sitemap lists it.
            priority: Its priority, from `0.1` to `1.0`.
            changefreq: How often it changes.

        Docs: https://docs.shoply.gg/api-reference/sitemap/update-one-address
        """
        return cast("Any", self._caller._call("sitemap.updateEntry", [], {"kind": kind, "ref": ref, "listed": listed, "priority": priority, "changefreq": changefreq}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class CartRecovery:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def show(
        self,
        *,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CartRecoveryShowResult:
        """**Get Cart Recovery**

        Cart Recovery's settings as `data`. `meta.figures` is the period's four figures: what it recovered, the checkouts left and what was in them, the share of emailed carts recovered, and the emails sent with how many buyers clicked and unsubscribed, each with the period before. `meta.set` is false where the store has never set it up, `meta.sendable` whether the store can send email at all, and `meta.choices` the delays and discounts each setting may take.

        Needs the `recovery.read` permission (Read Cart Recovery).

        Args:
            range: The period. Left out, it is "30d".
            from_: The first day of a period of your own, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Its last day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.

        Docs: https://docs.shoply.gg/api-reference/cart-recovery/get-cart-recovery
        """
        return cast("CartRecoveryShowResult", self._caller._call("cartRecovery.show", [], {"range": range, "from": from_, "to": to, "tz": tz}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        *,
        enabled: Optional[bool] = None,
        firstOn: Optional[bool] = None,
        firstMinutes: Optional[int] = None,
        firstSubject: Optional[str] = None,
        declinedOn: Optional[bool] = None,
        declinedMinutes: Optional[int] = None,
        declinedSubject: Optional[str] = None,
        secondOn: Optional[bool] = None,
        secondMinutes: Optional[int] = None,
        secondSubject: Optional[str] = None,
        secondPercent: Optional[int] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CartRecoveryUpdateResult:
        """**Change Cart Recovery**

        Changes the settings named and keeps the rest. Switching it on writes to nobody who left a checkout before: only checkouts started after it was switched on are followed. The first email goes out a while after the buyer left, or in its place the declined card email after a card was turned down; the second, later, carries a coupon made for that buyer, good for 48 hours. An empty subject is the email's own.

        Needs the `recovery.write` permission (Change Cart Recovery).

        Args:
            enabled: Whether Cart Recovery writes to buyers at all.
            firstOn: Whether the first email is sent.
            firstMinutes: Minutes after the buyer left. One of 30, 60, 120, 240.
            firstSubject: Its subject, up to 150 characters. It may hold the email's variables, such as `{{ store.name }}`; one whose marks cannot be read is refused.
            declinedOn: Whether the declined card email takes the first one's place after a card was turned down.
            declinedMinutes: Minutes after the decline. One of 5, 15, 30, 60.
            declinedSubject: Its subject, up to 150 characters. It may hold the email's variables, such as `{{ store.name }}`; one whose marks cannot be read is refused.
            secondOn: Whether the second email is sent.
            secondMinutes: Minutes after the buyer left. One of 720, 1200, 1440, 2880.
            secondSubject: Its subject, up to 150 characters. It may hold the email's variables, such as `{{ store.name }}`; one whose marks cannot be read is refused.
            secondPercent: The percent off its coupon. One of 0, 5, 10, 15, 20, 25. 0 sends it with no coupon.

        Docs: https://docs.shoply.gg/api-reference/cart-recovery/change-cart-recovery
        """
        return cast("CartRecoveryUpdateResult", self._caller._call("cartRecovery.update", [], {"enabled": enabled, "firstOn": firstOn, "firstMinutes": firstMinutes, "firstSubject": firstSubject, "declinedOn": declinedOn, "declinedMinutes": declinedMinutes, "declinedSubject": declinedSubject, "secondOn": secondOn, "secondMinutes": secondMinutes, "secondSubject": secondSubject, "secondPercent": secondPercent}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def carts(
        self,
        *,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        show: Optional[Literal["all", "waiting", "emailed", "recovered", "unsubscribed", "clicked"]] = None,
        search: Optional[str] = None,
        page: Optional[int] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[CartRecoveryCartsItem]:
        """**List carts**

        The checkouts buyers left in the period, newest first, 25 a page, each with where it stands. A cart's `id` is its checkout's order ID. `state` is `waiting` (its first email is to come, `note` says when), `not_emailed` (it will not be written to, `note` says why), `first`, `declined` or `second` (the email it last had), `recovered`, `unsubscribed`, or `stopped` (let go with nothing sent). `emailedAt` and `secondEmailAt` are when its emails went, `couponCode` the second email's coupon, `clickedAt` when a browser first opened its button, and `recoveredOrderId` and `recoveredAt` the order that paid: the cart's own, or the checkout its button opened.

        Needs the `recovery.read` permission (Read Cart Recovery).

        Args:
            range: The period. Left out, it is "30d".
            from_: The first day of a period of your own, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Its last day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.
            show: Only these. Left out, it is "all".
            search: Part of a buyer's email.
            page: Which page of the list. The first is 1. Left out, it is 1.

        Docs: https://docs.shoply.gg/api-reference/cart-recovery/list-carts
        """
        return cast("Page[CartRecoveryCartsItem]", self._caller._call("cartRecovery.carts", [], {"range": range, "from": from_, "to": to, "tz": tz, "show": show, "search": search, "page": page}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def cart(
        self,
        cart_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CartRecoveryCartResult:
        """**Get a cart**

        One cart as "List carts" has it, whatever its period. What the `cart.` webhooks send.

        Needs the `recovery.read` permission (Read Cart Recovery).

        Docs: https://docs.shoply.gg/api-reference/cart-recovery/get-a-cart
        """
        return cast("CartRecoveryCartResult", self._caller._call("cartRecovery.cart", [cart_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class WinBack:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def show(
        self,
        *,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> WinBackShowResult:
        """**Get Win-Back**

        Win-Back's settings as `data`. `meta.figures` is the period's four figures: the revenue it won back (and the period before's), subscribers and the share of buyers asked who said yes, the share of buyers emailed who came back, and the emails sent with how many buyers clicked and unsubscribed. `meta.set` is false where the store has never set it up, `meta.asking` whether the checkout asks buyers for leave, `meta.sendable` whether the store can send email at all, `meta.audiences` the tags it may be narrowed to, and `meta.choices` what each setting may take.

        Needs the `marketing.read` permission (Read Email Marketing).

        Args:
            range: The period. Left out, it is "30d".
            from_: The first day of a period of your own, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Its last day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.

        Docs: https://docs.shoply.gg/api-reference/email-marketing/get-win-back
        """
        return cast("WinBackShowResult", self._caller._call("winBack.show", [], {"range": range, "from": from_, "to": to, "tz": tz}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        *,
        enabled: Optional[bool] = None,
        firstOn: Optional[bool] = None,
        firstDays: Optional[int] = None,
        firstSubject: Optional[str] = None,
        secondOn: Optional[bool] = None,
        secondDays: Optional[int] = None,
        secondSubject: Optional[str] = None,
        secondPercent: Optional[int] = None,
        audience: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> WinBackUpdateResult:
        """**Change Win-Back**

        Changes the settings named and keeps the rest. Win-Back writes only to subscribers: buyers who ticked "Email me news and offers" at checkout on an order they paid, and have not said no since. The first email goes the set number of days after a buyer's last completed order, if they have not ordered since; the second, days after the first, carries a coupon made for that buyer, good for 7 days. A buyer with a dispute on record is not written to. Switching it on also switches on asking at checkout, and `meta.askingTurnedOn` says so. An empty subject is the email's own.

        Needs the `marketing.write` permission (Change Email Marketing).

        Args:
            enabled: Whether Win-Back writes to anybody.
            firstOn: Whether the first email is sent.
            firstDays: Days after a buyer's last order. One of 14, 21, 30, 45, 60, 90.
            firstSubject: Its subject, up to 150 characters. It may hold the email's variables, such as `{{ store.name }}`; one whose marks cannot be read is refused.
            secondOn: Whether the second email is sent.
            secondDays: Days after the first. One of 3, 7, 14, 21, 30.
            secondSubject: Its subject, up to 150 characters. It may hold the email's variables, such as `{{ store.name }}`; one whose marks cannot be read is refused.
            secondPercent: The percent off its coupon. One of 0, 5, 10, 15, 20, 25. 0 sends it with no coupon.
            audience: Who is written to: empty for every subscriber, `vip`, or the ID of one of the store's tags.

        Docs: https://docs.shoply.gg/api-reference/email-marketing/change-win-back
        """
        return cast("WinBackUpdateResult", self._caller._call("winBack.update", [], {"enabled": enabled, "firstOn": firstOn, "firstDays": firstDays, "firstSubject": firstSubject, "secondOn": secondOn, "secondDays": secondDays, "secondSubject": secondSubject, "secondPercent": secondPercent, "audience": audience}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def buyers(
        self,
        *,
        show: Optional[Literal["all", "due", "emailed", "won", "unsubscribed", "clicked"]] = None,
        search: Optional[str] = None,
        page: Optional[int] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[WinBackBuyersItem]:
        """**List Win-Back buyers**

        The buyers Win-Back has written to or will within 7 days, the latest to have moved first, 25 a page. A buyer is here once for each time they go quiet. `state` is `due` (`dueAt` says when its first email goes), `first` or `second` (the email it last had), `won` (they ordered within 14 days of an email: `wonOrderId`, `wonAt`, `wonAfter`, `quietDays`), `unsubscribed`, or `stopped` (`stopped` says why: `ordered`, `off`, `audience`, `disputed`, `failed`). `orders` and `spent` are their completed orders at the store, `tags` theirs as on Get a customer, `couponCode` and `couponExpiresAt` the second email's coupon, and `clickedAt` when a browser first opened an email's button.

        Needs the `marketing.read` permission (Read Email Marketing).

        Args:
            show: Only these. Left out, it is "all".
            search: Part of a buyer's email.
            page: Which page of the list. The first is 1. Left out, it is 1.

        Docs: https://docs.shoply.gg/api-reference/email-marketing/list-win-back-buyers
        """
        return cast("Page[WinBackBuyersItem]", self._caller._call("winBack.buyers", [], {"show": show, "search": search, "page": page}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def buyer(
        self,
        buyer_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> WinBackBuyerResult:
        """**Get a Win-Back buyer**

        One buyer as "List Win-Back buyers" has them. What the `winback.` webhooks send.

        Needs the `marketing.read` permission (Read Email Marketing).

        Docs: https://docs.shoply.gg/api-reference/email-marketing/get-a-win-back-buyer
        """
        return cast("WinBackBuyerResult", self._caller._call("winBack.buyer", [buyer_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Subscribers:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def summary(
        self,
        *,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SubscribersSummaryResult:
        """**Get subscriber figures**

        `asking`, whether the checkout asks buyers "Email me news and offers", and `figures` for the period: `subscribed` now, `joined` in the period, `asked` (paid orders whose box was shown) and `rate` (the share of those ticked), `unsubscribed` in the period, and `sent`, the emails Cart Recovery and Win-Back sent in it.

        Needs the `marketing.read` permission (Read Email Marketing).

        Args:
            range: The period. Left out, it is "30d".
            from_: The first day of a period of your own, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Its last day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.

        Docs: https://docs.shoply.gg/api-reference/email-marketing/get-subscriber-figures
        """
        return cast("SubscribersSummaryResult", self._caller._call("subscribers.summary", [], {"range": range, "from": from_, "to": to, "tz": tz}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def asking(
        self,
        *,
        on: bool,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SubscribersAskingResult:
        """**Change asking at checkout**

        Whether the checkout shows buyers an unticked box above Pay, "Email me news and offers from" the store, on checkouts they start on the store, in the embed and in the Checkout Kit. Never on an invoice or a payment link. Switched off, nobody new subscribes, and everybody subscribed stays so.

        Needs the `marketing.write` permission (Change Email Marketing).

        Args:
            on: Ask, or not. Required.

        Docs: https://docs.shoply.gg/api-reference/email-marketing/change-asking-at-checkout
        """
        return cast("SubscribersAskingResult", self._caller._call("subscribers.asking", [], {"on": on}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def list(
        self,
        *,
        show: Optional[Literal["all", "subscribed", "unsubscribed"]] = None,
        search: Optional[str] = None,
        page: Optional[int] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[SubscribersListItem]:
        """**List subscribers**

        Who said yes to the store's news and offers, newest first, 25 a page: `subscribedAt`, `source` and `where` (the store's checkout, the embed or the Checkout Kit), `orderId` (the order whose box was ticked; they became a subscriber when it was paid), and for one who said no since, `unsubscribedAt` and `unsubscribedBy` (`email`, a link in an email; `seller`; `key`).

        Needs the `marketing.read` permission (Read Email Marketing).

        Args:
            show: Only these. Left out, it is "all".
            search: Part of an email address.
            page: Which page of the list. The first is 1. Left out, it is 1.

        Docs: https://docs.shoply.gg/api-reference/email-marketing/list-subscribers
        """
        return cast("Page[SubscribersListItem]", self._caller._call("subscribers.list", [], {"show": show, "search": search, "page": page}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def export(
        self,
        *,
        show: Optional[Literal["all", "subscribed", "unsubscribed"]] = None,
        search: Optional[str] = None,
        check: Optional[Literal["1"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> File:
        """**Export subscribers**

        The subscribers the same filters would list, as a CSV file. Add `check=1` for `{ rows }`, how many it would have, which is not counted. A store exports at most 30 files every 10 minutes, every kind together, whoever asks: after that the answer is 429.

        Needs the `marketing.read` permission (Read Email Marketing). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Args:
            show: Only these. Left out, it is "all".
            search: Part of an email address.
            check: `1` for how many rows the file would have, as `{ rows }`, in place of the file.

        Docs: https://docs.shoply.gg/api-reference/email-marketing/export-subscribers
        """
        return cast("File", self._caller._call("subscribers.export", [], {"show": show, "search": search, "check": check}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def unsubscribe(
        self,
        *,
        email: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SubscribersUnsubscribeResult:
        """**Unsubscribe a subscriber**

        No more Win-Back to this address. They become a subscriber again only by ticking the box on another order they pay. 404 for an address that never said yes. Answers the subscriber.

        Needs the `marketing.write` permission (Change Email Marketing).

        Args:
            email: Their email address. Required.

        Docs: https://docs.shoply.gg/api-reference/email-marketing/unsubscribe-a-subscriber
        """
        return cast("SubscribersUnsubscribeResult", self._caller._call("subscribers.unsubscribe", [], {"email": email}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class EmailTemplates:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[EmailTemplatesListResultItem]:
        """**List email templates**

        Every email a store can write, in the order the dashboard lists them: its `kind`, `group`, `name`, `when` it is sent, whether the store has `edited` it (and which of `html`, `css` and `subject`), and `updatedAt`. `meta.shared` is the CSS every email gets (`css`, null where it is Shoply's look, `baseCss`), and `meta.sendable` whether the store can send email at all.

        Needs the `emails.read` permission (Read Email Templates).

        Docs: https://docs.shoply.gg/api-reference/email-templates/list-email-templates
        """
        return cast("List[EmailTemplatesListResultItem]", self._caller._call("emailTemplates.list", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def shared(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> EmailTemplatesSharedResult:
        """**Get the shared email CSS**

        The look every email gets but one with a `css` of its own, as `css` (null where it is Shoply's look), `updatedAt`, and Shoply's look as `baseCss`, `var(--accent)` in it for the shop's colour.

        Needs the `emails.read` permission (Read Email Templates).

        Docs: https://docs.shoply.gg/api-reference/email-templates/get-the-shared-email-css
        """
        return cast("EmailTemplatesSharedResult", self._caller._call("emailTemplates.shared", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def saveShared(
        self,
        *,
        css: str,
        expectedUpdatedAt: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> EmailTemplatesSaveSharedResult:
        """**Change the shared email CSS**

        The look every email gets but one with a `css` of its own, a whole sheet, checked as an email's own is; empty, null or `baseCss` as it is for none, which is Shoply's look. Saving one draws every email from its template, Shoply's original where the store has not written one.

        Needs the `emails.write` permission (Change Email Templates).

        Args:
            css: The whole look, or null for Shoply's. Required.
            expectedUpdatedAt: The `updatedAt` you read; one changed since is refused with `stale_write`.

        Docs: https://docs.shoply.gg/api-reference/email-templates/change-the-shared-email-css
        """
        return cast("EmailTemplatesSaveSharedResult", self._caller._call("emailTemplates.saveShared", [], {"css": css, "expectedUpdatedAt": expectedUpdatedAt}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def show(
        self,
        kind: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> EmailTemplatesShowResult:
        """**Get an email template**

        One email: what it is, its `variables` and `parts` (each a `name` and what it is), the marks it must hold (`required`), its `original` HTML, what the store has saved, `shared` (the CSS every email gets), `baseCss` (Shoply's look for the classes the originals are written with) and `accent` (the shop's colour, which `var(--accent)` is). The email is drawn with `css`, else `shared`, else `baseCss`. Each of `html`, `css` and `subject` is the store's own, or null where it is Shoply's original. A CSS is a whole look, never rules over another: an email is drawn with its own `css`, else the shared CSS, else Shoply's look (`baseCss`), where `var(--accent)` is the shop's colour. The HTML is the email's card and the lines under it, with Liquid's marks for what changes from one buyer to the next: `{{ order.id }}` prints a value, escaped, and `{{ parts.delivery }}` a part only Shoply writes. `variables` and `parts` say which an email has. Shoply writes the page round it, its dark look, and a last line under it, "Sent with Shoply", which no template changes. `originalSubject` is the original subject as a sample buyer would get it, and `originalSubjectSource` the same written with its variables.

        Needs the `emails.read` permission (Read Email Templates).

        Docs: https://docs.shoply.gg/api-reference/email-templates/get-an-email-template
        """
        return cast("EmailTemplatesShowResult", self._caller._call("emailTemplates.show", [kind], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        kind: str,
        *,
        html: Optional[str] = None,
        css: Optional[str] = None,
        subject: Optional[str] = None,
        expectedUpdatedAt: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> EmailTemplatesUpdateResult:
        """**Change an email template**

        Changes each of `html`, `css` and `subject` sent, and keeps the rest; null, an empty string, or the original's own HTML puts that one back to the original. Answers the email as Get an email template does. Refused with `template_problems` while anything would stop it, `problems` saying what and on which line, for `html`, `css` and `subject`. The HTML may hold the tags an email is made of, never a script, a form, a frame or <style>, and its links go to https, http, mailto or #, its pictures to https; up to 64 KB. Comments are taken out when it is sent, which `problems` says as a warning. The CSS is the email's whole look, and the shared CSS no longer changes an email that has one: start from `shared`, or `baseCss` where it is null. It sets how things look, with type, class, id and attribute selectors, and @media; no url(), no position, and no < or backslash; up to 32 KB. A subject is one line of up to 150 characters, and may hold the email's variables. Before it is saved the email is drawn for a sample buyer, and refused where it closes a <div> it never opened, where a mark it must hold is in its code but not in what it draws (inside a comment, or under a condition that is false), or where its subject comes out empty. Cart Recovery's and Win-Back's emails must hold `{{ links.unsubscribe }}`, and their subjects are those Change Cart Recovery and Change Win-Back set.

        Needs the `emails.write` permission (Change Email Templates).

        Args:
            html: The email's HTML, or null for the original.
            css: Its whole look, or null to follow the shared CSS. The look it would get anyway is saved as null.
            subject: Its subject, or null for the original.
            expectedUpdatedAt: The `updatedAt` you read; a template changed since is refused with `stale_write`.

        Docs: https://docs.shoply.gg/api-reference/email-templates/change-an-email-template
        """
        return cast("EmailTemplatesUpdateResult", self._caller._call("emailTemplates.update", [kind], {"html": html, "css": css, "subject": subject, "expectedUpdatedAt": expectedUpdatedAt}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def preview(
        self,
        kind: str,
        *,
        html: Optional[str] = None,
        css: Optional[str] = None,
        subject: Optional[str] = None,
        shared: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> EmailTemplatesPreviewResult:
        """**Preview an email template**

        The email for a sample buyer as it would be sent with what you send in place of what is saved: its `subject`, the whole page as `html`, its plain `text`, the `values` its variables had, and `problems` as Change an email template would say them. Nothing is saved and nothing is sent.

        Needs the `emails.read` permission (Read Email Templates).

        Args:
            html: HTML to preview in place of what is saved; null for the original.
            css: Its whole look, to preview in place of what is saved.
            subject: A subject to preview in place of what is saved.
            shared: The look every email gets, in place of what is saved.

        Docs: https://docs.shoply.gg/api-reference/email-templates/preview-an-email-template
        """
        return cast("EmailTemplatesPreviewResult", self._caller._call("emailTemplates.preview", [kind], {"html": html, "css": css, "subject": subject, "shared": shared}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def revert(
        self,
        kind: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> EmailTemplatesRevertResult:
        """**Revert an email template**

        Puts the email back as Shoply wrote it: its HTML, CSS and subject. Answers it as Get an email template does.

        Needs the `emails.write` permission (Change Email Templates).

        Docs: https://docs.shoply.gg/api-reference/email-templates/revert-an-email-template
        """
        return cast("EmailTemplatesRevertResult", self._caller._call("emailTemplates.revert", [kind], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Customers:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        page: Optional[int] = None,
        perPage: Optional[int] = None,
        search: Optional[str] = None,
        sort: Optional[Literal["newest", "spent", "orders", "recent", "balance"]] = None,
        only: Optional[Literal["affiliates", "subscribed"]] = None,
        tag: Optional[str] = None,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[CustomersListItem]:
        """**List customers**

        The store's customers, a page at a time, each with how many orders they have paid for, what they have spent, their balance and their `tags`: Shoply's two first (`vip` and `disputed`, worked out from their orders as they are read), then the store's own.

        Needs the `customers.read` permission (Read Customers).

        Args:
            page: Which page of the list. The first is 1. Left out, it is 1.
            perPage: How many a page holds. Left out, it is 20.
            search: Part of an email address.
            sort: What the list is ordered by, largest or latest first. Left out, it is "newest".
            only: Only customers who are affiliates, or who are subscribed to the store's news and offers.
            tag: Only customers wearing this tag: `vip`, `disputed`, or the ID of one of the store's own.
            range: Only customers first seen in this period.
            from_: Only customers first seen on or after this day, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Only customers first seen on or before this day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.

        Docs: https://docs.shoply.gg/api-reference/customers/list-customers
        """
        return cast("Page[CustomersListItem]", self._caller._call("customers.list", [], {"page": page, "perPage": perPage, "search": search, "sort": sort, "only": only, "tag": tag, "range": range, "from": from_, "to": to, "tz": tz}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        email: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomersCreateResult:
        """**Create a customer**

        Adds an address to the customer list before it has ordered, so it can be given a balance or made an affiliate. An address that is already a customer is answered as it is, with `meta.alreadyExisted` saying so.

        Needs the `customers.write` permission (Change Customers).

        Args:
            email: The customer's email address. Required.

        Docs: https://docs.shoply.gg/api-reference/customers/create-a-customer
        """
        return cast("CustomersCreateResult", self._caller._call("customers.create", [], {"email": email}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def export(
        self,
        *,
        search: Optional[str] = None,
        sort: Optional[Literal["newest", "spent", "orders", "recent", "balance"]] = None,
        only: Optional[Literal["affiliates", "subscribed"]] = None,
        tag: Optional[str] = None,
        check: Optional[Literal["1"]] = None,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> File:
        """**Export customers**

        The customers the same filters would list, as a CSV file: each one's email, when they were first seen, the orders they paid for and what they spent, their first and last paid order, their store balance, their affiliate code and balance where they have one, their tags, and whether they are subscribed to the store's news and offers. Every customer the filters match is in the file, however many: it is sent as it is read. Add `check=1` for `{ rows }`, how many it would have, which is not counted. A store exports at most 30 files every 10 minutes, orders, customers, fraud events and blacklist rules together, whoever asks: after that the answer is 429.

        Needs the `customers.read` permission (Read Customers). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Args:
            search: Part of an email address.
            sort: What the file is ordered by, largest or latest first. Left out, it is "newest".
            only: Only customers who are affiliates, or who are subscribed to the store's news and offers.
            tag: Only customers wearing this tag: `vip`, `disputed`, or the ID of one of the store's own.
            check: `1` for how many rows the file would have, as `{ rows }`, in place of the file. Not counted against the store's exports, and refused with 429 where none are left.
            range: Only customers first seen in this period.
            from_: Only customers first seen on or after this day, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Only customers first seen on or before this day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.

        Docs: https://docs.shoply.gg/api-reference/customers/export-customers
        """
        return cast("File", self._caller._call("customers.export", [], {"search": search, "sort": sort, "only": only, "tag": tag, "check": check, "range": range, "from": from_, "to": to, "tz": tz}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def stats(
        self,
        *,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomersStatsResult:
        """**Get customer figures**

        The four figures over the customers list, each beside the period before it. With no period named, the last 30 days.

        Needs the `customers.read` permission (Read Customers).

        Args:
            range: Only customers first seen in this period.
            from_: Only customers first seen on or after this day, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Only customers first seen on or before this day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.

        Docs: https://docs.shoply.gg/api-reference/customers/get-customer-figures
        """
        return cast("CustomersStatsResult", self._caller._call("customers.stats", [], {"range": range, "from": from_, "to": to, "tz": tz}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def show(
        self,
        customer_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomersShowResult:
        """**Get a customer**

        One customer: their orders, their balance and its history, their `tags`, whether they are blacklisted, and their affiliate figures if they are one.

        Needs the `customers.read` permission (Read Customers).

        Docs: https://docs.shoply.gg/api-reference/customers/get-a-customer
        """
        return cast("CustomersShowResult", self._caller._call("customers.show", [customer_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setBalance(
        self,
        customer_id: str,
        *,
        mode: Literal["add", "subtract", "set"],
        amount: float,
        note: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomersSetBalanceResult:
        """**Change a customer's balance**

        Adds to, takes from or sets the customer's balance at the store, which they can spend at checkout. Send an `Idempotency-Key` with this request, so that a retry does not credit twice. Answers the customer with the new balance and its history.

        Needs the `customers.balance` permission (Change Balances).

        Args:
            mode: Add to it, take from it, or set it to exactly this. Required.
            amount: How much, in the store's currency, with at most 2 decimals. Required.
            note: Why, up to 500 characters. Kept in the balance's history.

        Docs: https://docs.shoply.gg/api-reference/customers/change-a-customers-balance
        """
        return cast("CustomersSetBalanceResult", self._caller._call("customers.setBalance", [customer_id], {"mode": mode, "amount": amount, "note": note}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def blacklist(
        self,
        customer_id: str,
        *,
        addresses: Optional[bool] = None,
        note: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomersBlacklistResult:
        """**Blacklist a customer**

        Stops the customer buying: their email is added to the store's blacklist, and with `addresses` the IP addresses their orders came from. Their open checkouts are refused from this moment.

        Needs the `customers.write` permission (Change Customers).

        Args:
            addresses: Whether to blacklist the IP addresses their orders came from too, up to 20. Left out, it is true.
            note: Why. Kept with the rules it makes.

        Docs: https://docs.shoply.gg/api-reference/customers/blacklist-a-customer
        """
        return cast("CustomersBlacklistResult", self._caller._call("customers.blacklist", [customer_id], {"addresses": addresses, "note": note}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def unblacklist(
        self,
        customer_id: str,
        *,
        addresses: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomersUnblacklistResult:
        """**Clear a customer from the blacklist**

        Takes the customer off the blacklist: the rules their page or a dispute of theirs added, any rule on their email, and with `addresses` the rules on an IP address their orders came from. A rule that covers other buyers too (a domain, a range) stays: the customer's `blacklistedBy` lists each rule still refusing them.

        Needs the `customers.write` permission (Change Customers).

        Args:
            addresses: Whether to take off the rules on the IP addresses their orders came from too, which someone added by hand. Left out, it is true.

        Docs: https://docs.shoply.gg/api-reference/customers/clear-a-customer-from-the-blacklist
        """
        return cast("CustomersUnblacklistResult", self._caller._call("customers.unblacklist", [customer_id], {"addresses": addresses}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setTags(
        self,
        customer_id: str,
        *,
        tags: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CustomersSetTagsResultItem]:
        """**Set a customer's tags**

        The customer's own tags become exactly these: any not listed is taken off, any new one is put on, and each is sent as `customer.tagged` or `customer.untagged`. Shoply's two are not set here. Answers their tags.

        Needs the `customers.tags` permission (Change Tags).

        Args:
            tags: The IDs of the store's tags they wear. Required.

        Docs: https://docs.shoply.gg/api-reference/customers/set-a-customers-tags
        """
        return cast("List[CustomersSetTagsResultItem]", self._caller._call("customers.setTags", [customer_id], {"tags": tags}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def tag(
        self,
        customer_id: str,
        tag_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CustomersTagResultItem]:
        """**Put a tag on a customer**

        One of the store's tags on the customer. One they already wear changes nothing. Answers their tags.

        Needs the `customers.tags` permission (Change Tags).

        Docs: https://docs.shoply.gg/api-reference/customers/put-a-tag-on-a-customer
        """
        return cast("List[CustomersTagResultItem]", self._caller._call("customers.tag", [customer_id, tag_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def untag(
        self,
        customer_id: str,
        tag_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Union[List[Any], Dict[str, Any]]:
        """**Take a tag off a customer**

        One of the store's tags off the customer. One they do not wear changes nothing. Answers their tags.

        Needs the `customers.tags` permission (Change Tags).

        Docs: https://docs.shoply.gg/api-reference/customers/take-a-tag-off-a-customer
        """
        return cast("Union[List[Any], Dict[str, Any]]", self._caller._call("customers.untag", [customer_id, tag_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class CustomerTags:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CustomerTagsListResultItem]:
        """**List customer tags**

        The store's own tags as `data`, by name, each with `customers`, how many wear it. `meta.automatic` is Shoply's two: VIP's rule (`vipOn`, `vipSpent` in the store's currency, `vipOrders` completed orders, `vipDays` the period, 0 for all time; either number 0 leaves that half out) and `disputedOn`, with `vipCustomers` and `disputedCustomers`, how many wear each today.

        Needs the `customers.read` permission (Read Customers).

        Docs: https://docs.shoply.gg/api-reference/customers/list-customer-tags
        """
        return cast("List[CustomerTagsListResultItem]", self._caller._call("customerTags.list", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        name: str,
        tone: Optional[Literal["neutral", "primary", "success", "warning", "danger"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerTagsCreateResult:
        """**Add a customer tag**

        A tag of the store's own. A store has at most 50. Names are told apart without regard to case, and VIP and Disputed Before are Shoply's.

        Needs the `customers.tags` permission (Change Tags).

        Args:
            name: Its name, up to 32 characters. Required.
            tone: Its colour. Left out, it is "neutral".

        Docs: https://docs.shoply.gg/api-reference/customers/add-a-customer-tag
        """
        return cast("CustomerTagsCreateResult", self._caller._call("customerTags.create", [], {"name": name, "tone": tone}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def automatic(
        self,
        *,
        vipOn: Optional[bool] = None,
        vipSpent: Optional[float] = None,
        vipOrders: Optional[int] = None,
        vipDays: Optional[Literal[0, 365, 180, 90, 30]] = None,
        disputedOn: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CustomerTagsAutomaticResultItem]:
        """**Change VIP and Disputed Before**

        Shoply's two tags: whether each is put on, and who is a VIP. Both are worked out from a customer's orders whenever they are read, so a change reaches every customer at once. Answers as List customer tags does.

        Needs the `customers.tags` permission (Change Tags).

        Args:
            vipOn: Whether VIP is put on.
            vipSpent: A VIP has spent at least this, in the store's currency, on completed orders. 0 leaves it out.
            vipOrders: Or paid for at least this many orders. 0 leaves it out.
            vipDays: Over this many days back, 0 for all time.
            disputedOn: Whether Disputed Before is put on: a dispute on any of their orders, won or lost.

        Docs: https://docs.shoply.gg/api-reference/customers/change-vip-and-disputed-before
        """
        return cast("List[CustomerTagsAutomaticResultItem]", self._caller._call("customerTags.automatic", [], {"vipOn": vipOn, "vipSpent": vipSpent, "vipOrders": vipOrders, "vipDays": vipDays, "disputedOn": disputedOn}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        tag_id: str,
        *,
        name: Optional[str] = None,
        tone: Optional[Literal["neutral", "primary", "success", "warning", "danger"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerTagsUpdateResult:
        """**Change a customer tag**

        Renames a tag or changes its colour, keeping what is not sent. Everybody wearing it keeps it.

        Needs the `customers.tags` permission (Change Tags).

        Args:
            name: Its name, up to 32 characters.
            tone: Its colour.

        Docs: https://docs.shoply.gg/api-reference/customers/change-a-customer-tag
        """
        return cast("CustomerTagsUpdateResult", self._caller._call("customerTags.update", [tag_id], {"name": name, "tone": tone}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        tag_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Union[List[Any], Dict[str, Any]]:
        """**Delete a customer tag**

        Deletes a tag and takes it off everybody wearing it. No `customer.untagged` is sent for each. Win-Back narrowed to this tag writes to everybody subscribed again. Answers the tags left.

        Needs the `customers.tags` permission (Change Tags).

        Docs: https://docs.shoply.gg/api-reference/customers/delete-a-customer-tag
        """
        return cast("Union[List[Any], Dict[str, Any]]", self._caller._call("customerTags.delete", [tag_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Affiliates:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[AffiliatesListResultItem]:
        """**List affiliates**

        Every affiliate of the store, each with their link, their rates, what their link has led to, what they have earned and what they are owed. `meta.totals` adds them up, and `meta.programme` is the programme's settings. A store holds up to 500, so the list is not paged.

        Needs the `affiliates.read` permission (Read Affiliates).

        Docs: https://docs.shoply.gg/api-reference/affiliates/list-affiliates
        """
        return cast("List[AffiliatesListResultItem]", self._caller._call("affiliates.list", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        customer: str,
        code: Optional[str] = None,
        commission: Optional[float] = None,
        discount: Optional[float] = None,
        active: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> AffiliatesCreateResult:
        """**Create an affiliate**

        Makes a customer of the store an affiliate, with a link of their own. The address has to be a customer already: create the customer first if it is not.

        Needs the `affiliates.write` permission (Change Affiliates).

        Args:
            customer: The customer's email address. Required.
            code: What their link ends in: 2 to 40 letters, digits and dashes. One affiliate a code in a store.
            commission: The share of each order they earn, in percent: above 0, up to 90. It is taken on what the buyer paid for the products, after every discount, before fees and tax.
            discount: What their link takes off for the buyer, in percent: 0 to 90. Left out, it is 0.
            active: Whether their link works. Switched off, it takes nothing off and earns nothing.

        Docs: https://docs.shoply.gg/api-reference/affiliates/create-an-affiliate
        """
        return cast("AffiliatesCreateResult", self._caller._call("affiliates.create", [], {"customer": customer, "code": code, "commission": commission, "discount": discount, "active": active}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        affiliate_id: str,
        *,
        code: Optional[str] = None,
        commission: Optional[float] = None,
        discount: Optional[float] = None,
        active: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> AffiliatesUpdateResult:
        """**Update an affiliate**

        Changes an affiliate's code, rates or whether their link works. Only what is sent changes.

        Needs the `affiliates.write` permission (Change Affiliates).

        Args:
            code: What their link ends in: 2 to 40 letters, digits and dashes. One affiliate a code in a store.
            commission: The share of each order they earn, in percent: above 0, up to 90. It is taken on what the buyer paid for the products, after every discount, before fees and tax.
            discount: What their link takes off for the buyer, in percent: 0 to 90. Left out, it is 0.
            active: Whether their link works. Switched off, it takes nothing off and earns nothing.

        Docs: https://docs.shoply.gg/api-reference/affiliates/update-an-affiliate
        """
        return cast("AffiliatesUpdateResult", self._caller._call("affiliates.update", [affiliate_id], {"code": code, "commission": commission, "discount": discount, "active": active}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        affiliate_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[AffiliatesDeleteResultItem]:
        """**Delete an affiliate**

        Removes an affiliate who has earned nothing. One who has earned commission is refused with `affiliate_has_earned`: switch them off instead, so that what an order earned is still on record if that order is refunded later. Answers the affiliates that are left.

        Needs the `affiliates.write` permission (Change Affiliates).

        Docs: https://docs.shoply.gg/api-reference/affiliates/delete-an-affiliate
        """
        return cast("List[AffiliatesDeleteResultItem]", self._caller._call("affiliates.delete", [affiliate_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setBalance(
        self,
        affiliate_id: str,
        *,
        mode: Literal["add", "subtract", "set"],
        amount: float,
        note: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> AffiliatesSetBalanceResult:
        """**Change an affiliate's balance**

        Adds to, takes from or sets what an affiliate is owed. Send an `Idempotency-Key` with this request.

        Needs the `affiliates.payouts` permission (Answer Payouts).

        Args:
            mode: Add to it, take from it, or set it to exactly this. Required.
            amount: How much, in the store's currency, with at most 2 decimals. Required.
            note: Why, up to 500 characters. Kept in the balance's history.

        Docs: https://docs.shoply.gg/api-reference/affiliates/change-an-affiliates-balance
        """
        return cast("AffiliatesSetBalanceResult", self._caller._call("affiliates.setBalance", [affiliate_id], {"mode": mode, "amount": amount, "note": note}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def history(
        self,
        affiliate_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> AffiliatesHistoryResult:
        """**Get an affiliate's history**

        One affiliate's balance line by line (`changes`), and the payouts they have asked for (`payouts`).

        Needs the `affiliates.read` permission (Read Affiliates).

        Docs: https://docs.shoply.gg/api-reference/affiliates/get-an-affiliates-history
        """
        return cast("AffiliatesHistoryResult", self._caller._call("affiliates.history", [affiliate_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def orders(
        self,
        *,
        page: Optional[int] = None,
        perPage: Optional[int] = None,
        affiliate: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[Any]:
        """**List referred orders**

        The orders that came through affiliates' links, newest first, each with what it earned. `state` is `credited` (paid, and the commission is on the affiliate's balance), `waiting` (not paid yet) or `back` (refunded or charged back, and the commission taken back).

        Needs the `affiliates.read` permission (Read Affiliates).

        Args:
            page: Which page of the list. The first is 1. Left out, it is 1.
            perPage: How many a page holds. Left out, it is 25.
            affiliate: Only one affiliate's orders, by the affiliate's ID.

        Docs: https://docs.shoply.gg/api-reference/affiliates/list-referred-orders
        """
        return cast("Page[Any]", self._caller._call("affiliates.orders", [], {"page": page, "perPage": perPage, "affiliate": affiliate}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def payouts(
        self,
        *,
        page: Optional[int] = None,
        perPage: Optional[int] = None,
        status: Optional[Literal["requested", "paid", "declined", "cancelled"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[Any]:
        """**List payout requests**

        The payouts affiliates have asked for, the ones still waiting first. A payout is a request and a record: the affiliate says how they want to be paid, and the store pays it itself. Shoply sends no money.

        Needs the `affiliates.read` permission (Read Affiliates).

        Args:
            page: Which page of the list. The first is 1. Left out, it is 1.
            perPage: How many a page holds. Left out, it is 25.
            status: Only payouts in this status.

        Docs: https://docs.shoply.gg/api-reference/affiliates/list-payout-requests
        """
        return cast("Page[Any]", self._caller._call("affiliates.payouts", [], {"page": page, "perPage": perPage, "status": status}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def answerPayout(
        self,
        payout_id: str,
        *,
        action: Literal["paid", "declined"],
        note: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Answer a payout request**

        Marks a payout as paid, which records that you paid it yourself, or declines it, which puts the amount back on the affiliate's balance. A payout that was already answered is refused with `payout_answered`. Answers the store's affiliates as they now stand.

        Needs the `affiliates.payouts` permission (Answer Payouts).

        Args:
            action: What became of it. Required.
            note: For a declined payout, the reason. The affiliate reads it. Up to 500 characters.

        Docs: https://docs.shoply.gg/api-reference/affiliates/answer-a-payout-request
        """
        return cast("Any", self._caller._call("affiliates.answerPayout", [payout_id], {"action": action, "note": note}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def askPayout(
        self,
        affiliate_id: str,
        *,
        amount: float,
        details: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Ask for a payout for an affiliate**

        Asks for a payout in an affiliate's name, for a panel of your own where they sign in with you. The amount leaves their balance now and is held until you answer the request; declined or taken back, it returns. One request at a time, and never more than they are owed. Refused with `payout_refused` while the programme is off or does not take payout requests. Answers the request (`payout`) and what the affiliate is still owed (`balance`).

        Needs the `affiliates.payouts` permission (Answer Payouts).

        Args:
            amount: How much, above zero and up to what the affiliate is owed. Required.
            details: How they want to be paid, in their own words. Up to 300 characters. Required.

        Docs: https://docs.shoply.gg/api-reference/affiliates/ask-for-a-payout-for-an-affiliate
        """
        return cast("Any", self._caller._call("affiliates.askPayout", [affiliate_id], {"amount": amount, "details": details}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def withdrawPayout(
        self,
        affiliate_id: str,
        payout_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Take back a payout request**

        Takes back a request that has not been answered, and puts its amount back on the affiliate's balance. One that was already answered is refused with `payout_answered`.

        Needs the `affiliates.payouts` permission (Answer Payouts).

        Docs: https://docs.shoply.gg/api-reference/affiliates/take-back-a-payout-request
        """
        return cast("Any", self._caller._call("affiliates.withdrawPayout", [affiliate_id, payout_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def toStoreBalance(
        self,
        affiliate_id: str,
        *,
        amount: float,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Move commission to store balance**

        Moves what an affiliate is owed onto their balance at the store, to spend at checkout. It counts as paid out. What lands is what leaves: where the store balance is near its ceiling, less than was asked for moves, and `moved` says how much. Refused with `move_refused` while the programme is off or does not move commission to store balance.

        The key needs the `customers.balance` permission as well, since this adds to a customer's balance. Send an `Idempotency-Key` with this request.

        Needs the `affiliates.payouts` permission (Answer Payouts).

        Args:
            amount: How much, above zero and up to what the affiliate is owed. Required.

        Docs: https://docs.shoply.gg/api-reference/affiliates/move-commission-to-store-balance
        """
        return cast("Any", self._caller._call("affiliates.toStoreBalance", [affiliate_id], {"amount": amount}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class AffiliateProgramme:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def show(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> AffiliateProgrammeShowResult:
        """**Get the affiliate programme**

        The programme's settings: whether it is on, the rates a new affiliate gets, and what an affiliate may do for themselves.

        Needs the `affiliates.read` permission (Read Affiliates).

        Docs: https://docs.shoply.gg/api-reference/affiliates/get-the-affiliate-programme
        """
        return cast("AffiliateProgrammeShowResult", self._caller._call("affiliateProgramme.show", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        *,
        enabled: Optional[bool] = None,
        defaultCommission: Optional[float] = None,
        defaultDiscount: Optional[float] = None,
        selfSignup: Optional[bool] = None,
        ownLinks: Optional[bool] = None,
        toStore: Optional[bool] = None,
        payouts: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> AffiliateProgrammeUpdateResult:
        """**Update the affiliate programme**

        Changes the programme's settings. Only what is sent changes. Switched off, no link takes anything off or earns anything, and the customer panel says nothing of affiliates.

        Needs the `affiliates.write` permission (Change Affiliates).

        Args:
            enabled: Whether the programme is on.
            defaultCommission: The commission a new affiliate gets, in percent: above 0, up to 90.
            defaultDiscount: The discount a new affiliate's link gives buyers, in percent: 0 to 90.
            selfSignup: Whether a customer may join from the customer panel.
            ownLinks: Whether an affiliate may change the code their link ends in.
            toStore: Whether an affiliate may move commission to their store balance.
            payouts: Whether an affiliate may ask for a payout.

        Docs: https://docs.shoply.gg/api-reference/affiliates/update-the-affiliate-programme
        """
        return cast("AffiliateProgrammeUpdateResult", self._caller._call("affiliateProgramme.update", [], {"enabled": enabled, "defaultCommission": defaultCommission, "defaultDiscount": defaultDiscount, "selfSignup": selfSignup, "ownLinks": ownLinks, "toStore": toStore, "payouts": payouts}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Tickets:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        show: Optional[Literal["all", "unresolved", "open", "answered", "resolved"]] = None,
        search: Optional[str] = None,
        page: Optional[int] = None,
        perPage: Optional[int] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[TicketsListItem]:
        """**List support tickets**

        The store's tickets, the latest message first. `status` is `open` (the buyer wrote last: Waiting on You on the dashboard), `answered` (the store did) or `resolved`, with `resolvedBy`: `store`, `buyer`, or `auto` (48 hours after the store's reply with no word from the buyer). `lastFrom` and `lastLine` are the latest message's author and first words, `unread` whether the store has opened it since the buyer last wrote, and `orderId` the order it is about, where the buyer picked one. `meta.on` is whether the store takes tickets (off, buyers can open none and the panel shows no Support), and `meta.figures` the dashboard's four: tickets waiting on the store and when the oldest was written, open ones, the average minutes to a first reply over the last 30 days and the 30 before, and how many were resolved in the last 30 days.

        Needs the `tickets.read` permission (Read Support Tickets).

        Args:
            show: Only these: `unresolved` is `open` and `answered` together. Left out, it is "all".
            search: Part of the subject, the buyer's email or the latest message, or the start of the ticket's or the order's ID.
            page: Which page of the list. The first is 1. Left out, it is 1.
            perPage: How many a page holds, up to 100. Left out, it is 25.

        Docs: https://docs.shoply.gg/api-reference/support-tickets/list-support-tickets
        """
        return cast("Page[TicketsListItem]", self._caller._call("tickets.list", [], {"show": show, "search": search, "page": page, "perPage": perPage}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def settings(
        self,
        *,
        on: bool,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TicketsSettingsResult:
        """**Switch Support Tickets on or off**

        Off for every store until switched on. Off, buyers can open no ticket and write on none, the customer panel shows no Support, and the store can resolve and reopen but not reply. The tickets are kept.

        Needs the `tickets.write` permission (Answer Support Tickets).

        Args:
            on: Whether buyers can open tickets. Required.

        Docs: https://docs.shoply.gg/api-reference/support-tickets/switch-support-tickets-on-or-off
        """
        return cast("TicketsSettingsResult", self._caller._call("tickets.settings", [], {"on": on}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def get(
        self,
        ticket_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TicketsGetResult:
        """**Get a support ticket**

        A ticket with its `conversation`, oldest first: each message's `from` (`buyer` or `store`), `body` (Markdown, as written), `html` (the body as Markdown draws it, escaped: links only to the web or an email, each opening in a new tab, and a picture written in Markdown a link, never loaded), `pictures` (each one's `name` and the `url` the dashboard reads it at; read it with Get a ticket's picture) and `createdAt`. `customer` is who wrote it, with their tags, `order` the order it is about, `orders` their five latest, and `canReopenUntil` the last moment the buyer can open a resolved ticket again by writing on it. Reading a ticket marks it read, as opening it on the dashboard does.

        Needs the `tickets.read` permission (Read Support Tickets).

        Docs: https://docs.shoply.gg/api-reference/support-tickets/get-a-support-ticket
        """
        return cast("TicketsGetResult", self._caller._call("tickets.get", [ticket_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def reply(
        self,
        ticket_id: str,
        *,
        message: str,
        resolve: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TicketsReplyResult:
        """**Reply to a support ticket**

        Writes on the ticket as the store, which the buyer reads in their customer panel and is emailed (at most once a ticket in 15 minutes; what is written meanwhile follows when they are over). A reply to a resolved ticket opens it again, unless `resolve` is true. Refused with `tickets_off` while the store takes no tickets, since the buyer could not read it. Answers the ticket as Get a support ticket does.

        Needs the `tickets.write` permission (Answer Support Tickets).

        Args:
            message: The reply, up to 500 characters. Required.
            resolve: Mark the ticket resolved with the reply. Left out, it is false.

        Docs: https://docs.shoply.gg/api-reference/support-tickets/reply-to-a-support-ticket
        """
        return cast("TicketsReplyResult", self._caller._call("tickets.reply", [ticket_id], {"message": message, "resolve": resolve}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def resolve(
        self,
        ticket_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TicketsResolveResult:
        """**Resolve a support ticket**

        Marks it resolved, by the store. The buyer can still write on it for 30 days, which opens it again. One already resolved is left as it is.

        Needs the `tickets.write` permission (Answer Support Tickets).

        Docs: https://docs.shoply.gg/api-reference/support-tickets/resolve-a-support-ticket
        """
        return cast("TicketsResolveResult", self._caller._call("tickets.resolve", [ticket_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def reopen(
        self,
        ticket_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TicketsReopenResult:
        """**Reopen a support ticket**

        Opens a resolved ticket again: `open` where the buyer wrote last, else `answered`. One that is not resolved is left as it is.

        Needs the `tickets.write` permission (Answer Support Tickets).

        Docs: https://docs.shoply.gg/api-reference/support-tickets/reopen-a-support-ticket
        """
        return cast("TicketsReopenResult", self._caller._call("tickets.reopen", [ticket_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def picture(
        self,
        ticket_id: str,
        name: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> File:
        """**Get a ticket's picture**

        A picture sent in the conversation: a PNG, JPEG or WebP of up to 5 MB, read out of the picture itself when it was sent.

        Needs the `tickets.read` permission (Read Support Tickets).

        Docs: https://docs.shoply.gg/api-reference/support-tickets/get-a-tickets-picture
        """
        return cast("File", self._caller._call("tickets.picture", [ticket_id, name], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Team:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def get(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TeamGetResult:
        """**Get the team**

        The store's teams, each with its `permissions`, how many of them are `sensitive`, the parts of the dashboard it `reach`es, its `people` and how many invites are `waiting`; every `invite` not yet taken up; the store's `owner`, who is on no team and can do everything; and `permissions`, every permission there is in its `groups`, each with its `label`, what it lets a person do (`about`), whether it is `sensitive` and what it `needs`, and the `presets` a team can start from. `limits` says how many teams the store and people a team may have on its plan (invites not yet taken up counted among the people), how long a team's `name` may be, how many addresses one invite takes (`perInvite`) and how many days an invite lasts (`inviteDays`).

        Needs the `team.read` permission (Read the Team).

        Docs: https://docs.shoply.gg/api-reference/teams/get-the-team
        """
        return cast("TeamGetResult", self._caller._call("team.get", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def activity(
        self,
        *,
        person: Optional[str] = None,
        area: Optional[str] = None,
        page: Optional[int] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[TeamActivityItem]:
        """**List activity**

        Who did what at the store on the dashboard, the newest first, fifty a page: each line's `summary` ("Refunded order ..."), who did it as they were then (`name`, `email`, `team`, which is null for the owner), its `area` of the dashboard, and what it was about (`subject`). Every change and every export is a line, the owner's included; what a key does is not, and is in List API requests. Kept 365 days.

        Needs the `team.read` permission (Read the Team).

        Args:
            person: Only one person's, by their `userId`.
            area: Only one part of the dashboard, by its group's `id` in Get the team's `permissions`.
            page: Which page of the list. The first is 1. Left out, it is 1.

        Docs: https://docs.shoply.gg/api-reference/teams/list-activity
        """
        return cast("Page[TeamActivityItem]", self._caller._call("team.activity", [], {"person": person, "area": area, "page": page}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def invite(
        self,
        *,
        teamId: str,
        emails: Optional[List[str]] = None,
        kind: Optional[Literal["email", "link"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TeamInviteResult:
        """**Invite people**

        Emails an invite to each address in `emails`, up to 10 at a time, from Shoply. An invite is taken up only by an account with that address, which they sign in with or make, and the store is then in their store switcher. Each runs out in 7 days. `skipped` names an address left out and why: the owner's, one on the team already, or one invited already. With `kind` set to `link` instead, it makes a one-time link anybody can take up, answered in `url` here and never again. Not to a team that holds a sensitive permission: invite to one of those on the dashboard. The store's owner is emailed when somebody joins.

        Needs the `team.write` permission (Manage the Team). It sends an email, and is counted against a budget of its own: 60 in ten minutes for each key.

        Args:
            teamId: The team they join. Required.
            emails: The addresses to invite.
            kind: `link` for a one-time link in place of emails. Left out, it is "email".

        Docs: https://docs.shoply.gg/api-reference/teams/invite-people
        """
        return cast("TeamInviteResult", self._caller._call("team.invite", [], {"teamId": teamId, "emails": emails, "kind": kind}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def resendInvite(
        self,
        invite_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TeamResendInviteResult:
        """**Send an invite again**

        Sends an email invite again, or makes a link again (answered in `meta.url`), with 7 days from now. The address or link sent before stops working.

        Needs the `team.write` permission (Manage the Team). It sends an email, and is counted against a budget of its own: 60 in ten minutes for each key.

        Docs: https://docs.shoply.gg/api-reference/teams/send-an-invite-again
        """
        return cast("TeamResendInviteResult", self._caller._call("team.resendInvite", [invite_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def cancelInvite(
        self,
        invite_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TeamCancelInviteResult:
        """**Cancel an invite**

        Takes an invite back. Its email or link stops working.

        Needs the `team.write` permission (Manage the Team).

        Docs: https://docs.shoply.gg/api-reference/teams/cancel-an-invite
        """
        return cast("TeamCancelInviteResult", self._caller._call("team.cancelInvite", [invite_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def moveMember(
        self,
        member_id: str,
        *,
        teamId: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TeamMoveMemberResult:
        """**Move somebody to another team**

        They can do what the other team can from their next request. Not onto a team that holds a sensitive permission: do that on the dashboard.

        Needs the `team.write` permission (Manage the Team).

        Args:
            teamId: The team they move to. Required.

        Docs: https://docs.shoply.gg/api-reference/teams/move-somebody-to-another-team
        """
        return cast("TeamMoveMemberResult", self._caller._call("team.moveMember", [member_id], {"teamId": teamId}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def removeMember(
        self,
        member_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TeamRemoveMemberResult:
        """**Remove somebody from the team**

        They can no longer reach the store. The API keys they made and the apps they connected stop working with them (`keysStopped` says how many), and the webhooks those made are deleted.

        Needs the `team.write` permission (Manage the Team).

        Docs: https://docs.shoply.gg/api-reference/teams/remove-somebody-from-the-team
        """
        return cast("TeamRemoveMemberResult", self._caller._call("team.removeMember", [member_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Teams:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def create(
        self,
        *,
        name: str,
        permissions: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TeamsCreateResult:
        """**Create a team**

        A store holds as many teams as its plan does (`limits.teams` in Get the team). A permission marked `sensitive` that the team did not hold before cannot be given with a key: give it on the dashboard, which asks the person to confirm it is them.

        Needs the `team.write` permission (Manage the Team).

        Args:
            name: What the team is called, up to 40 characters, once a store. Required.
            permissions: What its people may do, by name (List the team answers every permission in `permissions`). What a permission leans on is added with it: `stock.edit` brings `stock.view` and `products.view`. Required.

        Docs: https://docs.shoply.gg/api-reference/teams/create-a-team
        """
        return cast("TeamsCreateResult", self._caller._call("teams.create", [], {"name": name, "permissions": permissions}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        team_id: str,
        *,
        name: str,
        permissions: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TeamsUpdateResult:
        """**Update a team**

        Saves the team whole: its name and its permissions. Its people can do what it now holds from their next request. A permission marked `sensitive` that the team did not hold before cannot be given with a key: give it on the dashboard, which asks the person to confirm it is them.

        Needs the `team.write` permission (Manage the Team).

        Args:
            name: What the team is called, up to 40 characters, once a store. Required.
            permissions: What its people may do, by name (List the team answers every permission in `permissions`). What a permission leans on is added with it: `stock.edit` brings `stock.view` and `products.view`. Required.

        Docs: https://docs.shoply.gg/api-reference/teams/update-a-team
        """
        return cast("TeamsUpdateResult", self._caller._call("teams.update", [team_id], {"name": name, "permissions": permissions}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        team_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TeamsDeleteResult:
        """**Delete a team**

        Refused with `team_not_empty` while anybody is on it: move or remove them first. Its invites not yet taken up go with it.

        Needs the `team.write` permission (Manage the Team).

        Docs: https://docs.shoply.gg/api-reference/teams/delete-a-team
        """
        return cast("TeamsDeleteResult", self._caller._call("teams.delete", [team_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Blacklist:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        page: Optional[int] = None,
        perPage: Optional[int] = None,
        status: Optional[Literal["enabled", "disabled"]] = None,
        type: Optional[Literal["email", "domain", "ip", "cidr", "asn", "isp", "city"]] = None,
        search: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[BlacklistListItem]:
        """**List blacklist rules**

        The store's blacklist, a page at a time. A buyer who matches a rule that is in force cannot start or pay for a checkout. A store holds up to 10,000 rules.

        Needs the `fraud.read` permission (Read Fraud Protection).

        Args:
            page: Which page of the list. The first is 1. Left out, it is 1.
            perPage: How many a page holds. Left out, it is 20.
            status: Only rules that are in force, or only ones switched off.
            type: Only rules of this type.
            search: Part of a rule's value or note.

        Docs: https://docs.shoply.gg/api-reference/blacklist/list-blacklist-rules
        """
        return cast("Page[BlacklistListItem]", self._caller._call("blacklist.list", [], {"page": page, "perPage": perPage, "status": status, "type": type, "search": search}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        type: Literal["email", "domain", "ip", "cidr", "asn", "isp", "city"],
        value: str,
        note: Optional[str] = None,
        enabled: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> BlacklistCreateResult:
        """**Create a blacklist rule**

        Adds a rule. Something already on the blacklist is refused.

        Needs the `fraud.write` permission (Change Fraud Protection).

        Args:
            type: What the rule matches: an email address, an email domain, an IP address, a range of them (`cidr`), a network by its number (`asn`) or its provider's name (`isp`), or a city. Countries are blocked in the settings instead. Required.
            value: What to match. Required.
            note: Why, up to 500 characters.
            enabled: Whether the rule is in force. Left out, it is true.

        Docs: https://docs.shoply.gg/api-reference/blacklist/create-a-blacklist-rule
        """
        return cast("BlacklistCreateResult", self._caller._call("blacklist.create", [], {"type": type, "value": value, "note": note, "enabled": enabled}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def export(
        self,
        *,
        status: Optional[Literal["enabled", "disabled"]] = None,
        type: Optional[Literal["email", "domain", "ip", "cidr", "asn", "isp", "city"]] = None,
        search: Optional[str] = None,
        check: Optional[Literal["1"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> File:
        """**Export blacklist rules**

        The rules the same filters would list, as a CSV file, newest first: each one's type, value and note, whether it is in force, when and how it was added, the customer or order it came from, and how many checkouts it has stopped. Every rule the filters match is in the file. Add `check=1` for `{ rows }`, how many it would have, which is not counted. A store exports at most 30 files every 10 minutes, orders, customers, fraud events and blacklist rules together, whoever asks: after that the answer is 429.

        Needs the `fraud.read` permission (Read Fraud Protection). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Args:
            status: Only rules that are in force, or only ones switched off.
            type: Only rules of this type.
            search: Part of a rule's value or note.
            check: `1` for how many rows the file would have, as `{ rows }`, in place of the file. Not counted against the store's exports, and refused with 429 where none are left.

        Docs: https://docs.shoply.gg/api-reference/blacklist/export-blacklist-rules
        """
        return cast("File", self._caller._call("blacklist.export", [], {"status": status, "type": type, "search": search, "check": check}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        rule_id: str,
        *,
        type: Literal["email", "domain", "ip", "cidr", "asn", "isp", "city"],
        value: str,
        note: Optional[str] = None,
        enabled: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> BlacklistUpdateResult:
        """**Update a blacklist rule**

        Saves the rule whole: send every field as it should be.

        Needs the `fraud.write` permission (Change Fraud Protection).

        Args:
            type: What the rule matches: an email address, an email domain, an IP address, a range of them (`cidr`), a network by its number (`asn`) or its provider's name (`isp`), or a city. Countries are blocked in the settings instead. Required.
            value: What to match. Required.
            note: Why, up to 500 characters.
            enabled: Whether the rule is in force. Left out, it is true.

        Docs: https://docs.shoply.gg/api-reference/blacklist/update-a-blacklist-rule
        """
        return cast("BlacklistUpdateResult", self._caller._call("blacklist.update", [rule_id], {"type": type, "value": value, "note": note, "enabled": enabled}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        rule_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> BlacklistDeleteResult:
        """**Delete a blacklist rule**

        Removes the rule.

        Needs the `fraud.write` permission (Change Fraud Protection).

        Docs: https://docs.shoply.gg/api-reference/blacklist/delete-a-blacklist-rule
        """
        return cast("BlacklistDeleteResult", self._caller._call("blacklist.delete", [rule_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setEnabled(
        self,
        rule_id: str,
        *,
        enabled: bool,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> BlacklistSetEnabledResult:
        """**Switch a blacklist rule on or off**

        Changes whether the rule is in force, without sending the rest of it.

        Needs the `fraud.write` permission (Change Fraud Protection).

        Args:
            enabled: Whether the rule is in force. Required.

        Docs: https://docs.shoply.gg/api-reference/blacklist/switch-a-blacklist-rule-on-or-off
        """
        return cast("BlacklistSetEnabledResult", self._caller._call("blacklist.setEnabled", [rule_id], {"enabled": enabled}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class FraudEvents:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        page: Optional[int] = None,
        perPage: Optional[int] = None,
        reason: Optional[Literal["blacklist", "vpn", "country", "unpaid_limit", "dispute", "refund", "changes"]] = None,
        search: Optional[str] = None,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[FraudEventsListItem]:
        """**List fraud events**

        What fraud protection did, newest first: the checkouts it refused and why, and every change to the blacklist and its settings. `meta.counts` says how many events of each reason the same filters match.

        Needs the `fraud.read` permission (Read Fraud Protection).

        Args:
            page: Which page of the list. The first is 1. Left out, it is 1.
            perPage: How many a page holds. Left out, it is 20.
            reason: Only events of this reason. `changes` is every change to the rules and settings.
            search: Part of an email address, an IP address or a rule's value.
            range: Only events in this period.
            from_: Only events on or after this day, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Only events on or before this day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.

        Docs: https://docs.shoply.gg/api-reference/fraud-protection/list-fraud-events
        """
        return cast("Page[FraudEventsListItem]", self._caller._call("fraudEvents.list", [], {"page": page, "perPage": perPage, "reason": reason, "search": search, "range": range, "from": from_, "to": to, "tz": tz}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def export(
        self,
        *,
        reason: Optional[Literal["blacklist", "vpn", "country", "unpaid_limit", "dispute", "refund", "changes"]] = None,
        search: Optional[str] = None,
        check: Optional[Literal["1"]] = None,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> File:
        """**Export fraud events**

        The events the same filters would list, as a CSV file, newest first: when each happened and how many attempts it gathered, what it was, the email, IP address, country and order, the rule it matched or the change that was made and by whom, and what a lookup of the address already knew (its provider and network, where it is, and whether it looked like a VPN, a data centre or a phone). Nothing is looked up to write the file: an address never looked up has those empty. Every event the filters match is in the file, however many: it is sent as it is read. Add `check=1` for `{ rows }`, how many it would have, which is not counted. A store exports at most 30 files every 10 minutes, orders, customers, fraud events and blacklist rules together, whoever asks: after that the answer is 429.

        Needs the `fraud.read` permission (Read Fraud Protection). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Args:
            reason: Only events of this reason. `changes` is every change to the rules and settings.
            search: Part of an email address, an IP address or a rule's value.
            check: `1` for how many rows the file would have, as `{ rows }`, in place of the file. Not counted against the store's exports, and refused with 429 where none are left.
            range: Only events in this period.
            from_: Only events on or after this day, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Only events on or before this day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.

        Docs: https://docs.shoply.gg/api-reference/fraud-protection/export-fraud-events
        """
        return cast("File", self._caller._call("fraudEvents.export", [], {"reason": reason, "search": search, "check": check, "range": range, "from": from_, "to": to, "tz": tz}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def network(
        self,
        event_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Get a fraud event's network**

        What is known about the connection an event came from: its provider, and whether it looks like a VPN, a proxy or a data centre.

        Needs the `fraud.read` permission (Read Fraud Protection). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Docs: https://docs.shoply.gg/api-reference/fraud-protection/get-a-fraud-events-network
        """
        return cast("Any", self._caller._call("fraudEvents.network", [event_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class FraudSettings:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def show(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> FraudSettingsShowResult:
        """**Get fraud settings**

        What the store refuses before an order is made: VPNs and proxies, countries, and buyers who have disputed a payment.

        Needs the `fraud.read` permission (Read Fraud Protection).

        Docs: https://docs.shoply.gg/api-reference/fraud-protection/get-fraud-settings
        """
        return cast("FraudSettingsShowResult", self._caller._call("fraudSettings.show", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        *,
        blockVpn: bool,
        blockOnDispute: Optional[bool] = None,
        blockedCountries: Optional[List[str]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> FraudSettingsUpdateResult:
        """**Update fraud settings**

        Saves the two switches as they are sent. `blockedCountries` changes only when it is sent.

        Needs the `fraud.write` permission (Change Fraud Protection).

        Args:
            blockVpn: Whether checkouts from a VPN, a proxy or a data centre are refused. Required.
            blockOnDispute: Whether a buyer who disputes a payment is blacklisted. Left out, it is true.
            blockedCountries: The countries checkouts are refused from, as two-letter codes. An empty list blocks none.

        Docs: https://docs.shoply.gg/api-reference/fraud-protection/update-fraud-settings
        """
        return cast("FraudSettingsUpdateResult", self._caller._call("fraudSettings.update", [], {"blockVpn": blockVpn, "blockOnDispute": blockOnDispute, "blockedCountries": blockedCountries}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Disputes:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        q: Optional[str] = None,
        show: Optional[Literal["all", "open", "needs_response", "under_review", "won", "lost", "accepted", "closed"]] = None,
        provider: Optional[str] = None,
        page: Optional[int] = None,
        perPage: Optional[int] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[DisputesListItem]:
        """**List disputes**

        The disputes buyers opened on the store's payments, as their payment providers reported them: the ones that need an answer first, soonest deadline first, then the rest newest first. `status` is how it reads on the dashboard: `needs_response`, `under_review`, `won`, `lost`, `accepted` or `closed` (ended with no chargeback). `providerStatus` is the provider's own last word, `stage` is `inquiry`, `chargeback`, `claim` (a PayPal case), `pre_arbitration` or `arbitration`, and `dueAt` when the provider stops taking an answer, where it says. `answeredFrom` is where it is answered: `here` (through this API: Stripe's, Revolut's, Adyen's, and PayPal's where PayPal is connected with API keys), `provider` (in the provider's own dashboard, named in `answerPlace`) or `none`. `meta.figures` is the dashboard's four: how many need an answer and how many are due within three days, the money in the open ones in the store's currency, how many ended won and lost in the last 90 days, and the orders disputed beside those that took money in that time.

        Needs the `disputes.read` permission (Read Disputes).

        Args:
            q: Part of the buyer's email, the order's ID or the provider's ID for the dispute.
            show: Only these: `open` is the two that have not ended. Left out, it is "all".
            provider: Only disputes with this payment method, by its ID.
            page: Which page of the list. The first is 1. Left out, it is 1.
            perPage: How many a page holds. Left out, it is 20.

        Docs: https://docs.shoply.gg/api-reference/disputes/list-disputes
        """
        return cast("Page[DisputesListItem]", self._caller._call("disputes.list", [], {"q": q, "show": show, "provider": provider, "page": page, "perPage": perPage}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def export(
        self,
        *,
        q: Optional[str] = None,
        show: Optional[Literal["all", "open", "needs_response", "under_review", "won", "lost", "accepted", "closed"]] = None,
        provider: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> File:
        """**Export disputes**

        The disputes the same filters would list, as a CSV file, newest first. Add `check=1` for `{ rows }`, how many it would have, which is not counted. A store exports at most 30 files every 10 minutes, whatever they are of and whoever asks: after that the answer is 429.

        Needs the `disputes.read` permission (Read Disputes). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Args:
            q: Part of the buyer's email, the order's ID or the provider's ID for the dispute.
            show: Only these: `open` is the two that have not ended. Left out, it is "all".
            provider: Only disputes with this payment method, by its ID.

        Docs: https://docs.shoply.gg/api-reference/disputes/export-disputes
        """
        return cast("File", self._caller._call("disputes.export", [], {"q": q, "show": show, "provider": provider}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def forOrder(
        self,
        order_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[DisputesForOrderResultItem]:
        """**List an order's disputes**

        The disputes on one order, newest first, each as List disputes has it. Most orders have none; a payment disputed twice has two.

        Needs the `disputes.read` permission (Read Disputes).

        Docs: https://docs.shoply.gg/api-reference/disputes/list-an-orders-disputes
        """
        return cast("List[DisputesForOrderResultItem]", self._caller._call("disputes.forOrder", [order_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def get(
        self,
        dispute_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> DisputesGetResult:
        """**Get a dispute**

        One dispute with everything its page shows. `records` is what Shoply recorded about the order, in four groups (the buyer, the order, after delivery, history), each fact a `name` and a `value` in words, `strong` on the order being opened again from the address it was paid from. A delivered license key or file is never in it. `activity` is every look at the order after delivery, a line each. `draft` is the store's answer as it was left, with `statement`, the whole of what is sent. `can` says what may be done now: `edit`, `submit`, `accept` and `markSubmitted`. `files` are the store's own files for the answer, `after` what was done on Shoply's side (the buyer blacklisted, their keys and files hidden), and `history` the dispute's story, newest first.

        Needs the `disputes.read` permission (Read Disputes).

        Docs: https://docs.shoply.gg/api-reference/disputes/get-a-dispute
        """
        return cast("DisputesGetResult", self._caller._call("disputes.get", [dispute_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def saveDraft(
        self,
        dispute_id: str,
        *,
        decision: Optional[Literal["fight", "accept"]] = None,
        contacted: Optional[Literal["", "yes", "no"]] = None,
        used: Optional[Literal["", "yes", "unknown"]] = None,
        words: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> DisputesSaveDraftResult:
        """**Save a dispute's answer**

        Keeps the fields named and leaves the rest, while the answer can still change: nothing has been sent or accepted, and the dispute has not ended. Answers 409 `not_answerable` after that. Sends nothing anywhere.

        Needs the `disputes.write` permission (Answer Disputes).

        Args:
            decision: Whether to fight it or accept it.
            contacted: Whether the buyer contacted the store before disputing. Empty when not said.
            used: Whether they used what they bought, or `unknown`. Empty when not said.
            words: The store's statement in its own words, up to 10,000 characters. Sent apart from what Shoply recorded.

        Docs: https://docs.shoply.gg/api-reference/disputes/save-a-disputes-answer
        """
        return cast("DisputesSaveDraftResult", self._caller._call("disputes.saveDraft", [dispute_id], {"decision": decision, "contacted": contacted, "used": used, "words": words}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def submit(
        self,
        dispute_id: str,
        *,
        decision: Optional[Literal["fight", "accept"]] = None,
        contacted: Optional[Literal["", "yes", "no"]] = None,
        used: Optional[Literal["", "yes", "unknown"]] = None,
        words: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Submit a dispute's answer**

        Sends a dispute's answer to its provider, once: what Shoply recorded, Shoply's PDF of it, the store's own files, and the statement, in each provider's own shape. Stripe's evidence fields; Revolut's files and a challenge whose comment is the statement's first 250 characters; PayPal's evidence, appeal or supporting information, whichever the dispute takes now, with the statement as its notes; Adyen's documents under a defense reason, the statement in the PDF. It cannot be taken back. Any draft fields in the body are saved first. Answers 409 `answered_elsewhere` for a dispute answered in its provider's own dashboard, `not_answerable` for one not waiting on an answer, `past_due` once its deadline has passed, and `file_not_taken` for one of the store's files the provider does not take (Adyen takes no PNG, and a PDF of up to 2 MB). The provider refusing it is 502, with `stripe_key` or `provider_key` where the store's key or app may not answer disputes, and `provider_refused` otherwise, the dispute back to a draft with `answer.note` saying why. A store sends at most 20 answers or acceptances every 10 minutes.

        Needs the `disputes.write` permission (Answer Disputes).

        Args:
            decision: Whether to fight it or accept it.
            contacted: Whether the buyer contacted the store before disputing. Empty when not said.
            used: Whether they used what they bought, or `unknown`. Empty when not said.
            words: The store's statement in its own words, up to 10,000 characters. Sent apart from what Shoply recorded.

        Docs: https://docs.shoply.gg/api-reference/disputes/submit-a-disputes-answer
        """
        return cast("Any", self._caller._call("disputes.submit", [dispute_id], {"decision": decision, "contacted": contacted, "used": used, "words": words}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def accept(
        self,
        dispute_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Accept a dispute**

        Concedes a dispute in its provider (Stripe, Revolut, Adyen, or PayPal's claim, which PayPal refunds from the store's account): the buyer keeps the money and the order becomes a chargeback. Cannot be undone. Answers as Submit does when it cannot be done, and counts toward the same 20 every 10 minutes.

        Needs the `disputes.write` permission (Answer Disputes).

        Docs: https://docs.shoply.gg/api-reference/disputes/accept-a-dispute
        """
        return cast("Any", self._caller._call("disputes.accept", [dispute_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def markSubmitted(
        self,
        dispute_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> DisputesMarkSubmittedResult:
        """**Mark a dispute as answered**

        Says the store answered a dispute in its provider's own dashboard (PayPal's Resolution Center, Revolut, Adyen, Whop, Shopify), which Shoply cannot send to. It then reads as under review, and its answer can no longer change. 409 `not_answerable` where it is not waiting on an answer there.

        Needs the `disputes.write` permission (Answer Disputes).

        Docs: https://docs.shoply.gg/api-reference/disputes/mark-a-dispute-as-answered
        """
        return cast("DisputesMarkSubmittedResult", self._caller._call("disputes.markSubmitted", [dispute_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def packet(
        self,
        dispute_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> File:
        """**Get a dispute's PDF**

        The answer as one PDF, as it stands: the dispute, the store's statement, what Shoply recorded, every look at the order after delivery, and the store's refund policy and terms. For a provider that takes a file. Never a license key or a delivered file.

        Needs the `disputes.read` permission (Read Disputes).

        Docs: https://docs.shoply.gg/api-reference/disputes/get-a-disputes-pdf
        """
        return cast("File", self._caller._call("disputes.packet", [dispute_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def addFile(
        self,
        dispute_id: str,
        *,
        file: Union[str, "os.PathLike[str]", bytes, BinaryIO],
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
        kind: Optional[Literal["communication", "receipt", "other"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Add a file to a dispute's answer**

        One of the store's own files for the answer, sent as `multipart/form-data` in a field called `file`: a PDF, a PNG or a JPEG, its type read from the file itself. One of each `kind`, a new one in place of the one there was, and all of a dispute's files together up to 4 MB, which with Shoply's PDF is within Stripe's limit. Sent to Stripe as `customer_communication`, `receipt` and `service_documentation`, and to Revolut, PayPal and Adyen beside Shoply's PDF. For a dispute answered to Adyen, a PNG is refused as `invalid_type`, and a PDF over 2 MB as `too_large`: Adyen takes neither. A store adds at most 30 files every 10 minutes.

        Needs the `disputes.write` permission (Answer Disputes).

        Args:
            file: A path on disk, the file's bytes, or a file opened for reading.
            filename: Its name. Left out, the path's own, or "upload".
            content_type: Its type, "image/png". Left out, worked out from the name.
            kind: What the file is: a chat with the buyer, a receipt, or something else. Left out, it is "other".

        Docs: https://docs.shoply.gg/api-reference/disputes/add-a-file-to-a-disputes-answer
        """
        return cast("Any", self._caller._call("disputes.addFile", [dispute_id], {"file": file, "filename": filename, "content_type": content_type, "kind": kind}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def deleteFile(
        self,
        dispute_id: str,
        file_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Remove a file from a dispute's answer**

        While the answer can still change.

        Needs the `disputes.write` permission (Answer Disputes).

        Docs: https://docs.shoply.gg/api-reference/disputes/remove-a-file-from-a-disputes-answer
        """
        return cast("Any", self._caller._call("disputes.deleteFile", [dispute_id, file_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def access(
        self,
        dispute_id: str,
        *,
        hidden: bool,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> DisputesAccessResult:
        """**Hide or show what an order delivered**

        Hides the order's license keys, files and instructions from its buyer for this dispute, on the order's page, in the customer panel and at its download links, or shows them again. What was emailed cannot be taken back. A dispute that is won shows them again by itself.

        Needs the `disputes.write` permission (Answer Disputes).

        Args:
            hidden: True to hide them, false to show them again. Required.

        Docs: https://docs.shoply.gg/api-reference/disputes/hide-or-show-what-an-order-delivered
        """
        return cast("DisputesAccessResult", self._caller._call("disputes.access", [dispute_id], {"hidden": hidden}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def blacklist(
        self,
        dispute_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> DisputesBlacklistResult:
        """**Blacklist a dispute's buyer**

        Puts the buyer's email and the addresses they ordered from on the blacklist, as a dispute does by itself where the store's settings say to. Rules already there are left as they are.

        Needs the `disputes.write` permission (Answer Disputes).

        Docs: https://docs.shoply.gg/api-reference/disputes/blacklist-a-disputes-buyer
        """
        return cast("DisputesBlacklistResult", self._caller._call("disputes.blacklist", [dispute_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def settings(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> DisputesSettingsResult:
        """**Get dispute settings**

        What happens by itself when a dispute opens, how one is answered, and who is told. Amounts are in the store's currency, `currency`.

        Needs the `disputes.read` permission (Read Disputes).

        Docs: https://docs.shoply.gg/api-reference/disputes/get-dispute-settings
        """
        return cast("DisputesSettingsResult", self._caller._call("disputes.settings", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def updateSettings(
        self,
        *,
        blacklist: Optional[bool] = None,
        takeBackAccess: Optional[bool] = None,
        acceptSmall: Optional[bool] = None,
        acceptUnder: Optional[float] = None,
        autoSubmit: Optional[bool] = None,
        askAboveOn: Optional[bool] = None,
        askAbove: Optional[float] = None,
        emailOpened: Optional[bool] = None,
        emailClosed: Optional[bool] = None,
        discord: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> DisputesUpdateSettingsResult:
        """**Change dispute settings**

        Changes the settings named and keeps the rest. Accepting small ones and submitting before the deadline are for disputes answered from Shoply (Stripe's, Revolut's, Adyen's, and PayPal's with API keys), and run every few minutes: a dispute under `acceptUnder` that nobody has started an answer for is accepted, and with a day left an answer is submitted as it stands, or where there is none, only when the buyer opened their order or took a file from the address they paid from. Nothing over `askAbove` is sent or accepted by itself where `askAboveOn` is on.

        Needs the `disputes.write` permission (Answer Disputes).

        Args:
            blacklist: Blacklist the buyer's email and addresses when a dispute opens.
            takeBackAccess: Hide what the order delivered from its buyer while a dispute is open, shown again if it is won.
            acceptSmall: Accept a dispute answered from Shoply under `acceptUnder` rather than fight it.
            acceptUnder: The amount, above 0.
            autoSubmit: Submit the answer of a dispute answered from Shoply with a day left.
            askAboveOn: Never send or accept one over `askAbove` by itself.
            askAbove: The amount, above 0, up to 1,000,000.
            emailOpened: Email the store when one opens, with its deadline.
            emailClosed: Email the store how one ended.
            discord: Post both to the store's Discord. Needs a webhook in its notification settings.

        Docs: https://docs.shoply.gg/api-reference/disputes/change-dispute-settings
        """
        return cast("DisputesUpdateSettingsResult", self._caller._call("disputes.updateSettings", [], {"blacklist": blacklist, "takeBackAccess": takeBackAccess, "acceptSmall": acceptSmall, "acceptUnder": acceptUnder, "autoSubmit": autoSubmit, "askAboveOn": askAboveOn, "askAbove": askAbove, "emailOpened": emailOpened, "emailClosed": emailClosed, "discord": discord}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Finance:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def access(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> FinanceAccessResult:
        """**Get finance access**

        Whether the store may use Finance yet (`open`), and what its business details still lack if not (`missing`). They are set in the dashboard's settings.

        Needs the `finance.read` permission (Read Finance).

        Docs: https://docs.shoply.gg/api-reference/finance/get-finance-access
        """
        return cast("FinanceAccessResult", self._caller._call("finance.access", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def profit(
        self,
        *,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> FinanceProfitResult:
        """**Get profit**

        What the store kept in a period and how that is made up, beside the period before: net sales, the cost of goods, payment fees, affiliate commission, expenses and net profit, twelve months of sales and profit, and every product with what each variant sold and cost. A sale is what the buyer paid: at its sale price, after its coupon and any affiliate link's discount, without tax. Payment fees are worked out from the rates the store typed, never read from a provider, so they can be slightly off. A store makes at most 20 reports every 10 minutes, counting this one, the other report, their files and the dashboard's Generate Report together: after that the answer is 429. Refused with `business_details_required` until the store has its business details.

        Needs the `finance.read` permission (Read Finance). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Args:
            range: The period. Left out, it is "this_month".
            from_: The first day of a period of your own, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Its last day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.

        Docs: https://docs.shoply.gg/api-reference/finance/get-profit
        """
        return cast("FinanceProfitResult", self._caller._call("finance.profit", [], {"range": range, "from": from_, "to": to, "tz": tz}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def accounting(
        self,
        *,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> FinanceAccountingResult:
        """**Get the books**

        The books for a period: the profit and loss line by line beside the period before, where the buyers were, and what each payment method took in. Gross sales are at the prices before any sale, and what sales, discounts, refunds and chargebacks took off is a line each; affiliate commission is a cost of sales. Tax collected is not income and is in none of it but the tax report. A store makes at most 20 reports every 10 minutes, counting this one, the other report, their files and the dashboard's Generate Report together: after that the answer is 429. Refused with `business_details_required` until the store has its business details.

        Needs the `finance.read` permission (Read Finance). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Args:
            range: The period. Left out, it is "this_month".
            from_: The first day of a period of your own, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Its last day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.

        Docs: https://docs.shoply.gg/api-reference/finance/get-the-books
        """
        return cast("FinanceAccountingResult", self._caller._call("finance.accounting", [], {"range": range, "from": from_, "to": to, "tz": tz}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def export(
        self,
        what: str,
        *,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        format: Optional[Literal["csv"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> File:
        """**Export the books**

        One of a period's files: `statement` (the profit and loss as a PDF, or as a CSV with `format=csv`), `countries`, `transactions` or `tax` (each a CSV), or `pack`, a ZIP of all of them with the expenses beside them. A store makes at most 20 reports every 10 minutes, counting this one, the other report, their files and the dashboard's Generate Report together: after that the answer is 429. Refused with `business_details_required` until the store has its business details.

        Needs the `finance.read` permission (Read Finance). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Args:
            range: The period. Left out, it is "this_month".
            from_: The first day of a period of your own, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Its last day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.
            format: For `statement`: `csv` for a spreadsheet in place of the PDF.

        Docs: https://docs.shoply.gg/api-reference/finance/export-the-books
        """
        return cast("File", self._caller._call("finance.export", [what], {"range": range, "from": from_, "to": to, "tz": tz, "format": format}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setCost(
        self,
        variant_id: str,
        *,
        amount: Optional[float] = None,
        percent: Optional[float] = None,
        applyToPast: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> FinanceSetCostResult:
        """**Set a variant's cost**

        What one sale of a variant costs the store, as an amount or as a share of what it sold for: what the buyer paid for it, after its sale price and discounts, without tax. Send neither to clear it. The cost is stamped onto each order line when the order is paid, so a later change does not rewrite old months. Refused with `business_details_required` until the store has its business details.

        Needs the `finance.write` permission (Change Finance).

        Args:
            amount: The cost of one, in the store's currency.
            percent: Or the cost as a percent of what each one sold for.
            applyToPast: Whether to give this cost to the lines already sold that have none. `past` in the answer says how many such lines there are. Left out, it is false.

        Docs: https://docs.shoply.gg/api-reference/finance/set-a-variants-cost
        """
        return cast("FinanceSetCostResult", self._caller._call("finance.setCost", [variant_id], {"amount": amount, "percent": percent, "applyToPast": applyToPast}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def paymentCosts(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> FinancePaymentCostsResult:
        """**Get payment fee rates**

        The rate the store has typed for each payment provider: what that provider keeps of a payment, as a percent and a fixed amount. Profit takes payment fees from these. Refused with `business_details_required` until the store has its business details.

        Needs the `finance.read` permission (Read Finance).

        Docs: https://docs.shoply.gg/api-reference/finance/get-payment-fee-rates
        """
        return cast("FinancePaymentCostsResult", self._caller._call("finance.paymentCosts", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setPaymentCosts(
        self,
        *,
        rates: List[Dict[str, Any]],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[FinanceSetPaymentCostsResultItem]:
        """**Set payment fee rates**

        Saves the rates for the providers named. A refusal names the provider and the field: `stripe.percent`. Refused with `business_details_required` until the store has its business details.

        Needs the `finance.write` permission (Change Finance).

        Args:
            rates: A rate a provider. Required.

        Docs: https://docs.shoply.gg/api-reference/finance/set-payment-fee-rates
        """
        return cast("List[FinanceSetPaymentCostsResultItem]", self._caller._call("finance.setPaymentCosts", [], {"rates": rates}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Tax:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def show(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TaxShowResult:
        """**Get tax settings**

        Whether the store collects tax at checkout, whether its prices include it, the places it collects in and at what rate, and each country's built-in rate. Refused with `business_details_required` until the store has its business details.

        Needs the `finance.read` permission (Read Finance).

        Docs: https://docs.shoply.gg/api-reference/tax/get-tax-settings
        """
        return cast("TaxShowResult", self._caller._call("tax.show", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        *,
        collect: Optional[bool] = None,
        included: Optional[bool] = None,
        business: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TaxUpdateResult:
        """**Update tax settings**

        Changes the store's three tax switches. Only what is sent changes. Refused with `business_details_required` until the store has its business details.

        Needs the `finance.write` permission (Change Finance).

        Args:
            collect: Whether tax is charged at checkout.
            included: Whether the store's prices already include the tax. Off, it is added on top.
            business: Whether a business buyer's VAT number takes the tax off, when the EU's register confirms it and it is from another country than the store's.

        Docs: https://docs.shoply.gg/api-reference/tax/update-tax-settings
        """
        return cast("TaxUpdateResult", self._caller._call("tax.update", [], {"collect": collect, "included": included, "business": business}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setRates(
        self,
        *,
        places: List[Dict[str, Any]],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TaxSetRatesResult:
        """**Add or change tax rates**

        Adds each place the store collects tax in, or changes its rate where it already does. The United States is taxed a state at a time. Answers the tax settings as they now stand. Refused with `business_details_required` until the store has its business details.

        Needs the `finance.write` permission (Change Finance).

        Args:
            places: The places. Required.

        Docs: https://docs.shoply.gg/api-reference/tax/add-or-change-tax-rates
        """
        return cast("TaxSetRatesResult", self._caller._call("tax.setRates", [], {"places": places}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def deleteRate(
        self,
        *,
        country: str,
        region: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> TaxDeleteRateResult:
        """**Remove a tax rate**

        Stops collecting tax in a place. A country named with no state goes with all of its states. Answers the tax settings as they now stand. Refused with `business_details_required` until the store has its business details.

        Needs the `finance.write` permission (Change Finance).

        Args:
            country: The country, as a two-letter code. Required.
            region: One state of it. Left out, the whole country.

        Docs: https://docs.shoply.gg/api-reference/tax/remove-a-tax-rate
        """
        return cast("TaxDeleteRateResult", self._caller._call("tax.deleteRate", [], {"country": country, "region": region}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Expenses:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        search: Optional[str] = None,
        category: Optional[str] = None,
        method: Optional[Literal["card", "bank", "crypto", "paypal", "cash", "other"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[ExpensesListResultItem]:
        """**List expenses**

        A period's expenses, newest first, up to 2,000 of them. `meta.totals` is what the expenses matched come to, counting every one, and `meta.groups` the same by category. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.read` permission (Read Expenses).

        Args:
            range: The period. Left out, it is "this_month".
            from_: The first day of a period of your own, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Its last day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.
            search: Part of a payee, a note or a reference.
            category: Only expenses in this expense category, by its ID.
            method: Only expenses paid this way.

        Docs: https://docs.shoply.gg/api-reference/expenses/list-expenses
        """
        return cast("List[ExpensesListResultItem]", self._caller._call("expenses.list", [], {"range": range, "from": from_, "to": to, "tz": tz, "search": search, "category": category, "method": method}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        spentOn: str,
        payee: str,
        amount: float,
        currency: Optional[str] = None,
        method: Optional[Literal["card", "bank", "crypto", "paypal", "cash", "other"]] = None,
        categoryId: Optional[str] = None,
        category: Optional[str] = None,
        note: Optional[str] = None,
        reference: Optional[str] = None,
        productId: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ExpensesCreateResult:
        """**Create an expense**

        Files an expense: what a bot paid a member of staff, a provider's invoice a script read. A store holds up to 50,000. A recurring expense is set up with its own route. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Args:
            spentOn: The day it was paid, as `YYYY-MM-DD`. Not in the future: a bill still to come is a recurring expense. Required.
            payee: Who was paid, up to 120 characters. Required.
            amount: How much, above zero, with at most 2 decimals. Required.
            currency: The currency `amount` is in, when it is not the store's own. It is converted at today's rate and kept in the store's currency.
            method: How it was paid.
            categoryId: The expense category it is filed in, by ID.
            category: The same, by the category's name, for a script that has no reason to know an ID. With neither, the store's rules file it.
            note: A note, up to 255 characters.
            reference: An invoice number or the like, up to 160 characters.
            productId: A product this expense is a cost of.

        Docs: https://docs.shoply.gg/api-reference/expenses/create-an-expense
        """
        return cast("ExpensesCreateResult", self._caller._call("expenses.create", [], {"spentOn": spentOn, "payee": payee, "amount": amount, "currency": currency, "method": method, "categoryId": categoryId, "category": category, "note": note, "reference": reference, "productId": productId}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def summary(
        self,
        *,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ExpensesSummaryResult:
        """**Get an expense summary**

        A period's spending at a glance: the total beside the period before, what repeats, the largest category, how many have receipts, twelve months of totals and what is coming up. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.read` permission (Read Expenses). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Args:
            range: The period. Left out, it is "this_month".
            from_: The first day of a period of your own, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Its last day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.

        Docs: https://docs.shoply.gg/api-reference/expenses/get-an-expense-summary
        """
        return cast("ExpensesSummaryResult", self._caller._call("expenses.summary", [], {"range": range, "from": from_, "to": to, "tz": tz}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def setup(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ExpensesSetupResult:
        """**Get what an expense can be**

        What an expense is made from: the store's expense categories, who it has paid before, the ways of paying, the currencies an amount can be sent in, and every limit. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.read` permission (Read Expenses).

        Docs: https://docs.shoply.gg/api-reference/expenses/get-what-an-expense-can-be
        """
        return cast("ExpensesSetupResult", self._caller._call("expenses.setup", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def export(
        self,
        *,
        range: Optional[Literal["today", "yesterday", "7d", "30d", "this_week", "last_week", "this_month", "last_month", "this_year"]] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        tz: Optional[str] = None,
        search: Optional[str] = None,
        category: Optional[str] = None,
        method: Optional[Literal["card", "bank", "crypto", "paypal", "cash", "other"]] = None,
        format: Optional[Literal["csv", "pdf"]] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> File:
        """**Export expenses**

        The expenses the same filters would list, as a CSV file or as a PDF on the store's letterhead. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.read` permission (Read Expenses). It is one of the heavier reads, and is counted against a smaller budget of its own: 60 a minute for each key.

        Args:
            range: The period. Left out, it is "this_month".
            from_: The first day of a period of your own, as `YYYY-MM-DD`. With `to`, in place of `range`.
            to: Its last day, as `YYYY-MM-DD`.
            tz: The time zone those days are in, as an IANA name. Left out, UTC.
            search: Part of a payee, a note or a reference.
            category: Only expenses in this expense category, by its ID.
            method: Only expenses paid this way.
            format: A spreadsheet or a document. Left out, it is "csv".

        Docs: https://docs.shoply.gg/api-reference/expenses/export-expenses
        """
        return cast("File", self._caller._call("expenses.export", [], {"range": range, "from": from_, "to": to, "tz": tz, "search": search, "category": category, "method": method, "format": format}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        expense_id: str,
        *,
        spentOn: str,
        payee: str,
        amount: float,
        currency: Optional[str] = None,
        method: Optional[Literal["card", "bank", "crypto", "paypal", "cash", "other"]] = None,
        categoryId: Optional[str] = None,
        category: Optional[str] = None,
        note: Optional[str] = None,
        reference: Optional[str] = None,
        productId: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ExpensesUpdateResult:
        """**Update an expense**

        Changes an expense. A field left out stays as it is. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Args:
            spentOn: The day it was paid, as `YYYY-MM-DD`. Not in the future: a bill still to come is a recurring expense. Required.
            payee: Who was paid, up to 120 characters. Required.
            amount: How much, above zero, with at most 2 decimals. Required.
            currency: The currency `amount` is in, when it is not the store's own. It is converted at today's rate and kept in the store's currency.
            method: How it was paid.
            categoryId: The expense category it is filed in, by ID.
            category: The same, by the category's name, for a script that has no reason to know an ID. With neither, the store's rules file it.
            note: A note, up to 255 characters.
            reference: An invoice number or the like, up to 160 characters.
            productId: A product this expense is a cost of.

        Docs: https://docs.shoply.gg/api-reference/expenses/update-an-expense
        """
        return cast("ExpensesUpdateResult", self._caller._call("expenses.update", [expense_id], {"spentOn": spentOn, "payee": payee, "amount": amount, "currency": currency, "method": method, "categoryId": categoryId, "category": category, "note": note, "reference": reference, "productId": productId}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        expense_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ExpensesDeleteResult:
        """**Delete an expense**

        Removes an expense, and its receipt with it. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Docs: https://docs.shoply.gg/api-reference/expenses/delete-an-expense
        """
        return cast("ExpensesDeleteResult", self._caller._call("expenses.delete", [expense_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def receipt(
        self,
        expense_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Get an expense's receipt**

        A link to the expense's receipt that works for five minutes. A receipt is private: there is no address for it that lasts. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.read` permission (Read Expenses).

        Docs: https://docs.shoply.gg/api-reference/expenses/get-an-expenses-receipt
        """
        return cast("Any", self._caller._call("expenses.receipt", [expense_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def addReceipt(
        self,
        expense_id: str,
        *,
        name: str,
        size: int,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Start a receipt upload**

        The first of three steps to attach a receipt: a PDF, PNG, JPG or WEBP. This one says what the file is and answers a signed address to send it to. Then send the file to that address with a `PUT`. Then call "Finish a receipt upload". Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Args:
            name: The file's name, with its ending. Required.
            size: Its size in bytes. Required.

        Docs: https://docs.shoply.gg/api-reference/expenses/start-a-receipt-upload
        """
        return cast("Any", self._caller._call("expenses.addReceipt", [expense_id], {"name": name, "size": size}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def deleteReceipt(
        self,
        expense_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Delete an expense's receipt**

        Removes the receipt and keeps the expense. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Docs: https://docs.shoply.gg/api-reference/expenses/delete-an-expenses-receipt
        """
        return cast("Any", self._caller._call("expenses.deleteReceipt", [expense_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def finishReceipt(
        self,
        expense_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Finish a receipt upload**

        The last step of attaching a receipt: says the file has been sent. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Docs: https://docs.shoply.gg/api-reference/expenses/finish-a-receipt-upload
        """
        return cast("Any", self._caller._call("expenses.finishReceipt", [expense_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class ExpenseCategories:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[ExpenseCategoriesListResultItem]:
        """**List expense categories**

        The categories the store files its expenses in, in its own order. A store holds up to 50. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.read` permission (Read Expenses).

        Docs: https://docs.shoply.gg/api-reference/expense-setup/list-expense-categories
        """
        return cast("List[ExpenseCategoriesListResultItem]", self._caller._call("expenseCategories.list", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        name: str,
        icon: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ExpenseCategoriesCreateResult:
        """**Create an expense category**

        Adds a category to file expenses in. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Args:
            name: Its name, up to 60 characters. Required.
            icon: The icon the dashboard draws beside it, from the list in "Get what an expense can be". Left out, it is "tag".

        Docs: https://docs.shoply.gg/api-reference/expense-setup/create-an-expense-category
        """
        return cast("ExpenseCategoriesCreateResult", self._caller._call("expenseCategories.create", [], {"name": name, "icon": icon}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        category_id: str,
        *,
        name: str,
        icon: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ExpenseCategoriesUpdateResult:
        """**Update an expense category**

        Renames a category or changes its icon. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Args:
            name: Its name. Required.
            icon: Its icon. Left out, it stays as it is.

        Docs: https://docs.shoply.gg/api-reference/expense-setup/update-an-expense-category
        """
        return cast("ExpenseCategoriesUpdateResult", self._caller._call("expenseCategories.update", [category_id], {"name": name, "icon": icon}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        category_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ExpenseCategoriesDeleteResult:
        """**Delete an expense category**

        Removes the category. The expenses filed under it stay, in no category: `moved` says how many. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Docs: https://docs.shoply.gg/api-reference/expense-setup/delete-an-expense-category
        """
        return cast("ExpenseCategoriesDeleteResult", self._caller._call("expenseCategories.delete", [category_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def sort(
        self,
        *,
        categoryIds: List[str],
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ExpenseCategoriesSortResult:
        """**Sort expense categories**

        Sets the order the categories are listed in. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Args:
            categoryIds: The categories' IDs in their new order. Required.

        Docs: https://docs.shoply.gg/api-reference/expense-setup/sort-expense-categories
        """
        return cast("ExpenseCategoriesSortResult", self._caller._call("expenseCategories.sort", [], {"categoryIds": categoryIds}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class RecurringExpenses:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[RecurringExpensesListResultItem]:
        """**List recurring expenses**

        The expenses that come round every month or year, with the day each is next due. A store holds up to 100. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.read` permission (Read Expenses).

        Docs: https://docs.shoply.gg/api-reference/expense-setup/list-recurring-expenses
        """
        return cast("List[RecurringExpensesListResultItem]", self._caller._call("recurringExpenses.list", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        payee: str,
        amount: float,
        cadence: Literal["month", "year"],
        nextOn: str,
        method: Optional[Literal["card", "bank", "crypto", "paypal", "cash", "other"]] = None,
        categoryId: Optional[str] = None,
        note: Optional[str] = None,
        reference: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> RecurringExpensesCreateResult:
        """**Create a recurring expense**

        Adds an expense that comes round. When it falls due it waits to be answered: paid, or skipped this once. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Args:
            payee: Who is paid, up to 120 characters. Required.
            amount: How much each time, in the store's currency. Required.
            cadence: How often it comes round. Required.
            nextOn: The day it is next due, as `YYYY-MM-DD`. Required.
            method: How it is paid.
            categoryId: The expense category it is filed in.
            note: A note, up to 255 characters.
            reference: A reference, up to 160 characters.

        Docs: https://docs.shoply.gg/api-reference/expense-setup/create-a-recurring-expense
        """
        return cast("RecurringExpensesCreateResult", self._caller._call("recurringExpenses.create", [], {"payee": payee, "amount": amount, "cadence": cadence, "nextOn": nextOn, "method": method, "categoryId": categoryId, "note": note, "reference": reference}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        recurring_id: str,
        *,
        payee: str,
        amount: float,
        cadence: Literal["month", "year"],
        nextOn: str,
        method: Optional[Literal["card", "bank", "crypto", "paypal", "cash", "other"]] = None,
        categoryId: Optional[str] = None,
        note: Optional[str] = None,
        reference: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> RecurringExpensesUpdateResult:
        """**Update a recurring expense**

        Changes a recurring expense. A field left out stays as it is. The expenses it has already written are not changed. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Args:
            payee: Who is paid, up to 120 characters. Required.
            amount: How much each time, in the store's currency. Required.
            cadence: How often it comes round. Required.
            nextOn: The day it is next due, as `YYYY-MM-DD`. Required.
            method: How it is paid.
            categoryId: The expense category it is filed in.
            note: A note, up to 255 characters.
            reference: A reference, up to 160 characters.

        Docs: https://docs.shoply.gg/api-reference/expense-setup/update-a-recurring-expense
        """
        return cast("RecurringExpensesUpdateResult", self._caller._call("recurringExpenses.update", [recurring_id], {"payee": payee, "amount": amount, "cadence": cadence, "nextOn": nextOn, "method": method, "categoryId": categoryId, "note": note, "reference": reference}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        recurring_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> RecurringExpensesDeleteResult:
        """**Delete a recurring expense**

        Stops it coming round. The expenses it has already written stay. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Docs: https://docs.shoply.gg/api-reference/expense-setup/delete-a-recurring-expense
        """
        return cast("RecurringExpensesDeleteResult", self._caller._call("recurringExpenses.delete", [recurring_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def paid(
        self,
        recurring_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Mark a recurring expense as paid**

        Answers one that is due: it was paid. The expense is filed under the day it fell due, and the recurring expense moves to its next date. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Docs: https://docs.shoply.gg/api-reference/expense-setup/mark-a-recurring-expense-as-paid
        """
        return cast("Any", self._caller._call("recurringExpenses.paid", [recurring_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def skip(
        self,
        recurring_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> RecurringExpensesSkipResult:
        """**Skip a recurring expense**

        Answers one that is due: not this time. Nothing is filed, and it moves to its next date. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Docs: https://docs.shoply.gg/api-reference/expense-setup/skip-a-recurring-expense
        """
        return cast("RecurringExpensesSkipResult", self._caller._call("recurringExpenses.skip", [recurring_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class ExpenseRules:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[ExpenseRulesListResultItem]:
        """**List expense rules**

        The store's rules for filing an expense that names no category: a phrase in the payee, and the category it means. A store holds up to 100. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.read` permission (Read Expenses).

        Docs: https://docs.shoply.gg/api-reference/expense-setup/list-expense-rules
        """
        return cast("List[ExpenseRulesListResultItem]", self._caller._call("expenseRules.list", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        phrase: str,
        categoryId: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ExpenseRulesCreateResult:
        """**Create an expense rule**

        Adds a rule: an expense whose payee contains the phrase is filed in the category. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Args:
            phrase: What to look for in a payee. Required.
            categoryId: The expense category it means. Required.

        Docs: https://docs.shoply.gg/api-reference/expense-setup/create-an-expense-rule
        """
        return cast("ExpenseRulesCreateResult", self._caller._call("expenseRules.create", [], {"phrase": phrase, "categoryId": categoryId}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        rule_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ExpenseRulesDeleteResult:
        """**Delete an expense rule**

        Removes the rule. Expenses it has already filed stay where they are. Refused with `business_details_required` until the store has its business details.

        Needs the `expenses.write` permission (Change Expenses).

        Docs: https://docs.shoply.gg/api-reference/expense-setup/delete-an-expense-rule
        """
        return cast("ExpenseRulesDeleteResult", self._caller._call("expenseRules.delete", [rule_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Requests:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        page: Optional[int] = None,
        perPage: Optional[int] = None,
        keyId: Optional[str] = None,
        method: Optional[Literal["GET", "POST", "PUT", "PATCH", "DELETE"]] = None,
        status: Optional[str] = None,
        search: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[RequestsListItem]:
        """**List API requests**

        The requests made with this store's API keys, newest first, without what was sent or answered. Requests are kept for 30 days. `meta.keptDays` says so.

        Needs the `logs.read` permission (Read API Requests).

        Args:
            page: Which page of the list. The first is 1. Left out, it is 1.
            perPage: How many a page holds, up to 100. Left out, it is 50.
            keyId: Only requests made with this API key.
            method: Only requests of this method.
            status: Only requests that worked (`ok`), that were refused or failed (`failed`), or with one status code (`404`).
            search: A request's ID, or part of a path.

        Docs: https://docs.shoply.gg/api-reference/api-requests/list-api-requests
        """
        return cast("Page[RequestsListItem]", self._caller._call("requests.list", [], {"page": page, "perPage": perPage, "keyId": keyId, "method": method, "status": status, "search": search}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def show(
        self,
        request_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> RequestsShowResult:
        """**Get an API request**

        One request, with what was sent and what came back. Long bodies are cut short, and values that are secrets or goods (a password, license keys going into stock) are not kept. A request's ID is the `X-Request-Id` header of its answer.

        Needs the `logs.read` permission (Read API Requests).

        Docs: https://docs.shoply.gg/api-reference/api-requests/get-an-api-request
        """
        return cast("RequestsShowResult", self._caller._call("requests.show", [request_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class Webhooks:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[WebhooksListResultItem]:
        """**List webhook endpoints**

        The store's webhook endpoints, each with the events it is sent and how its last delivery went. `recentDeliveries` is how its last twenty stand, oldest first: `delivered`, `failed` or `pending`. `meta.events` is every event there is. A store holds up to 20 endpoints.

        Needs the `webhooks.read` permission (Read Webhooks).

        Docs: https://docs.shoply.gg/api-reference/webhook-endpoints/list-webhook-endpoints
        """
        return cast("List[WebhooksListResultItem]", self._caller._call("webhooks.list", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        url: str,
        events: List[str],
        description: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> WebhooksCreateResult:
        """**Create a webhook endpoint**

        Adds an address for the store's events to be sent to. `secret` in the answer is what every delivery to it is signed with: it is answered here and never again, so keep it. The store's owner is told by email that a webhook was added.

        Needs the `webhooks.write` permission (Change Webhooks).

        Args:
            url: The https address deliveries are posted to. It cannot point at a private network, and it may name port 80, 443, 8080 or 8443. Required.
            events: The events it is sent, by name, or `["*"]` for every event there is and every one there will be. Required.
            description: A note for whoever manages the store, up to 160 characters.

        Docs: https://docs.shoply.gg/api-reference/webhook-endpoints/create-a-webhook-endpoint
        """
        return cast("WebhooksCreateResult", self._caller._call("webhooks.create", [], {"url": url, "events": events, "description": description}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def show(
        self,
        endpoint_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> WebhooksShowResult:
        """**Get a webhook endpoint**

        One endpoint. Never its signing secret.

        Needs the `webhooks.read` permission (Read Webhooks).

        Docs: https://docs.shoply.gg/api-reference/webhook-endpoints/get-a-webhook-endpoint
        """
        return cast("WebhooksShowResult", self._caller._call("webhooks.show", [endpoint_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def update(
        self,
        endpoint_id: str,
        *,
        url: str,
        events: List[str],
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> WebhooksUpdateResult:
        """**Update a webhook endpoint**

        Saves the endpoint whole: its address, its events and its note. `enabled` stays as it is when left out. Switching an endpoint on is also what starts one again that Shoply had paused for failing. Its signing secret stays the same.

        Needs the `webhooks.write` permission (Change Webhooks).

        Args:
            url: The https address deliveries are posted to. It cannot point at a private network, and it may name port 80, 443, 8080 or 8443. Required.
            events: The events it is sent, by name, or `["*"]` for every event there is and every one there will be. Required.
            description: A note for whoever manages the store, up to 160 characters.
            enabled: Whether events are sent to it. Switched off, nothing is sent, and what happens meanwhile is not kept for it.

        Docs: https://docs.shoply.gg/api-reference/webhook-endpoints/update-a-webhook-endpoint
        """
        return cast("WebhooksUpdateResult", self._caller._call("webhooks.update", [endpoint_id], {"url": url, "events": events, "description": description, "enabled": enabled}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def delete(
        self,
        endpoint_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> WebhooksDeleteResult:
        """**Delete a webhook endpoint**

        Removes the endpoint, and with it the record of what was sent to it.

        Needs the `webhooks.write` permission (Change Webhooks).

        Docs: https://docs.shoply.gg/api-reference/webhook-endpoints/delete-a-webhook-endpoint
        """
        return cast("WebhooksDeleteResult", self._caller._call("webhooks.delete", [endpoint_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def rotateSecret(
        self,
        endpoint_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Replace a signing secret**

        Gives the endpoint a new signing secret, answered here and never again. The old one signs nothing from this moment, so give your server the new one before its next delivery is checked.

        Needs the `webhooks.write` permission (Change Webhooks).

        Docs: https://docs.shoply.gg/api-reference/webhook-endpoints/replace-a-signing-secret
        """
        return cast("Any", self._caller._call("webhooks.rotateSecret", [endpoint_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def test(
        self,
        endpoint_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Send a test delivery**

        Sends a `webhook.test` event to the endpoint now, whatever it subscribes to, and answers what your server said. It is signed like any other and is in the delivery log. A store may ask for 30 test and resent deliveries in ten minutes.

        Needs the `webhooks.write` permission (Change Webhooks).

        Docs: https://docs.shoply.gg/api-reference/webhook-endpoints/send-a-test-delivery
        """
        return cast("Any", self._caller._call("webhooks.test", [endpoint_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class WebhookDeliveries:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        page: Optional[int] = None,
        perPage: Optional[int] = None,
        endpointId: Optional[str] = None,
        event: Optional[str] = None,
        state: Optional[Literal["pending", "delivered", "failed"]] = None,
        search: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Page[Any]:
        """**List webhook deliveries**

        What was sent to the store's endpoints, newest first, without the bodies. A delivery is one event on its way to one endpoint: `pending` while it is being tried, then `delivered` or `failed`. Deliveries are kept for 30 days.

        Needs the `webhooks.read` permission (Read Webhooks).

        Args:
            page: Which page of the list. The first is 1. Left out, it is 1.
            perPage: How many a page holds, up to 100. Left out, it is 50.
            endpointId: Only deliveries to this endpoint.
            event: Only deliveries of this event.
            state: Only deliveries in this state.
            search: A delivery's ID, an event's ID, or the ID of what the event is about, such as an order.

        Docs: https://docs.shoply.gg/api-reference/webhook-deliveries/list-webhook-deliveries
        """
        return cast("Page[Any]", self._caller._call("webhookDeliveries.list", [], {"page": page, "perPage": perPage, "endpointId": endpointId, "event": event, "state": state, "search": search}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def show(
        self,
        delivery_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Get a webhook delivery**

        One delivery, with the body that was sent (`payload`) and every try at sending it (`tries`): the status your server answered with, the start of what it answered, or why it could not be reached.

        Needs the `webhooks.read` permission (Read Webhooks).

        Docs: https://docs.shoply.gg/api-reference/webhook-deliveries/get-a-webhook-delivery
        """
        return cast("Any", self._caller._call("webhookDeliveries.show", [delivery_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def resend(
        self,
        delivery_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Resend a webhook delivery**

        Sends the same body again, to the endpoint's address and under its secret as they are now, and answers the delivery with the new try in it. The delivery's ID is the same, so a server that has already taken it can tell.

        Needs the `webhooks.write` permission (Change Webhooks).

        Docs: https://docs.shoply.gg/api-reference/webhook-deliveries/resend-a-webhook-delivery
        """
        return cast("Any", self._caller._call("webhookDeliveries.resend", [delivery_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class ClientResources:
    """The routes, as resources and methods.
    """
    key: Key
    store: Store
    domain: Domain
    paymentMethods: PaymentMethods
    analytics: Analytics
    storefronts: Storefronts
    routing: Routing
    customMethods: CustomMethods
    products: Products
    productImages: ProductImages
    stock: Stock
    categories: Categories
    upsells: Upsells
    subscriptions: Subscriptions
    orders: Orders
    invoices: Invoices
    reviews: Reviews
    coupons: Coupons
    couponCategories: CouponCategories
    couponPopup: CouponPopup
    sales: Sales
    blog: Blog
    blogCategories: BlogCategories
    blogPosts: BlogPosts
    seo: Seo
    redirects: Redirects
    brokenLinks: BrokenLinks
    sitemap: Sitemap
    cartRecovery: CartRecovery
    winBack: WinBack
    subscribers: Subscribers
    emailTemplates: EmailTemplates
    customers: Customers
    customerTags: CustomerTags
    affiliates: Affiliates
    affiliateProgramme: AffiliateProgramme
    tickets: Tickets
    team: Team
    teams: Teams
    blacklist: Blacklist
    fraudEvents: FraudEvents
    fraudSettings: FraudSettings
    disputes: Disputes
    finance: Finance
    tax: Tax
    expenses: Expenses
    expenseCategories: ExpenseCategories
    recurringExpenses: RecurringExpenses
    expenseRules: ExpenseRules
    requests: Requests
    webhooks: Webhooks
    webhookDeliveries: WebhookDeliveries

    def _call(self, id: str, path: List[str], fields: Dict[str, Any], options: Dict[str, Any]) -> Any:
        raise NotImplementedError

    def _resources(self) -> None:
        self.key = Key(self)
        self.store = Store(self)
        self.domain = Domain(self)
        self.paymentMethods = PaymentMethods(self)
        self.analytics = Analytics(self)
        self.storefronts = Storefronts(self)
        self.routing = Routing(self)
        self.customMethods = CustomMethods(self)
        self.products = Products(self)
        self.productImages = ProductImages(self)
        self.stock = Stock(self)
        self.categories = Categories(self)
        self.upsells = Upsells(self)
        self.subscriptions = Subscriptions(self)
        self.orders = Orders(self)
        self.invoices = Invoices(self)
        self.reviews = Reviews(self)
        self.coupons = Coupons(self)
        self.couponCategories = CouponCategories(self)
        self.couponPopup = CouponPopup(self)
        self.sales = Sales(self)
        self.blog = Blog(self)
        self.blogCategories = BlogCategories(self)
        self.blogPosts = BlogPosts(self)
        self.seo = Seo(self)
        self.redirects = Redirects(self)
        self.brokenLinks = BrokenLinks(self)
        self.sitemap = Sitemap(self)
        self.cartRecovery = CartRecovery(self)
        self.winBack = WinBack(self)
        self.subscribers = Subscribers(self)
        self.emailTemplates = EmailTemplates(self)
        self.customers = Customers(self)
        self.customerTags = CustomerTags(self)
        self.affiliates = Affiliates(self)
        self.affiliateProgramme = AffiliateProgramme(self)
        self.tickets = Tickets(self)
        self.team = Team(self)
        self.teams = Teams(self)
        self.blacklist = Blacklist(self)
        self.fraudEvents = FraudEvents(self)
        self.fraudSettings = FraudSettings(self)
        self.disputes = Disputes(self)
        self.finance = Finance(self)
        self.tax = Tax(self)
        self.expenses = Expenses(self)
        self.expenseCategories = ExpenseCategories(self)
        self.recurringExpenses = RecurringExpenses(self)
        self.expenseRules = ExpenseRules(self)
        self.requests = Requests(self)
        self.webhooks = Webhooks(self)
        self.webhookDeliveries = WebhookDeliveries(self)


class CustomerOrders:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def show(
        self,
        order_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerOrdersShowResult:
        """**Get an order**

        One of the buyer's orders, as its page in the customer panel shows it: each line, and once it is completed what it delivered (keys, the answers of a dynamic delivery, files with their download links, instructions). An order of another address answers as one that does not exist.

        Keys and files are left out while the store holds them back: an ended or paused subscription's order, or one whose payment is disputed. `productPath` is the product's path on the store's own site. Opening an order is recorded for the store, as on its order page, as a look from the store's own site.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 300 reads in ten minutes.

        Docs: https://docs.shoply.gg/api-reference/customer-api/get-an-order
        """
        return cast("CustomerOrdersShowResult", self._caller._call("customer.orders.show", [order_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class CustomerAffiliatePayouts:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def create(
        self,
        *,
        amount: float,
        details: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerAffiliatePayoutsCreateResult:
        """**Ask for a payout**

        Asks the seller to pay the affiliate, where the store allows payouts. The amount comes off their affiliate balance now and goes back if the seller declines or the request is taken back. One at a time. Shoply moves no money: the seller pays it and marks it paid.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 30 changes in ten minutes.

        Args:
            amount: How much, in the store's currency, up to their affiliate balance. Required.
            details: How they want to be paid, in their own words. Required.

        Docs: https://docs.shoply.gg/api-reference/customer-api/ask-for-a-payout
        """
        return cast("CustomerAffiliatePayoutsCreateResult", self._caller._call("customer.affiliate.payouts.create", [], {"amount": amount, "details": details}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def cancel(
        self,
        payout_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerAffiliatePayoutsCancelResult:
        """**Take back a payout request**

        Takes back a request the seller has not answered, and puts its amount back on the affiliate balance. One already answered is `payout_answered`.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 30 changes in ten minutes.

        Docs: https://docs.shoply.gg/api-reference/customer-api/take-back-a-payout-request
        """
        return cast("CustomerAffiliatePayoutsCancelResult", self._caller._call("customer.affiliate.payouts.cancel", [payout_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class CustomerAffiliate:
    payouts: CustomerAffiliatePayouts

    def __init__(self, caller: Any) -> None:
        self._caller = caller
        self.payouts = CustomerAffiliatePayouts(caller)

    def show(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerAffiliateShowResult:
        """**Get the affiliate page**

        The buyer as an affiliate of the store: their link and its code, their rates, clicks and orders, what they have earned, their affiliate balance, their payouts and its history, and what the store lets them do (`can`). One who is not an affiliate is answered `member: false` with what joining would give them, where the store lets buyers join. A store with no programme answers `no_programme`.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 300 reads in ten minutes.

        Docs: https://docs.shoply.gg/api-reference/customer-api/get-the-affiliate-page
        """
        return cast("CustomerAffiliateShowResult", self._caller._call("customer.affiliate.show", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def join(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerAffiliateJoinResult:
        """**Join the affiliate programme**

        Makes the buyer an affiliate at the store's own rates, with a link that works at once, where the store lets buyers join. Answers the affiliate page.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 30 changes in ten minutes.

        Docs: https://docs.shoply.gg/api-reference/customer-api/join-the-affiliate-programme
        """
        return cast("CustomerAffiliateJoinResult", self._caller._call("customer.affiliate.join", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def link(
        self,
        *,
        code: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerAffiliateLinkResult:
        """**Change the link's code**

        What the affiliate's link ends in, where the store lets affiliates choose it. The old link stops working. Answers the affiliate page.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 30 changes in ten minutes.

        Args:
            code: What the link ends in: letters, digits and dashes, as long as `limits` on the affiliate page says. One affiliate a code in a store. Required.

        Docs: https://docs.shoply.gg/api-reference/customer-api/change-the-links-code
        """
        return cast("CustomerAffiliateLinkResult", self._caller._call("customer.affiliate.link", [], {"code": code}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def toStore(
        self,
        *,
        amount: float,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerAffiliateToStoreResult:
        """**Move commission to store balance**

        Moves commission from the affiliate balance to the buyer's store balance, to spend at checkout, where the store allows it.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 30 changes in ten minutes.

        Args:
            amount: How much, in the store's currency, up to their affiliate balance. Required.

        Docs: https://docs.shoply.gg/api-reference/customer-api/move-commission-to-store-balance
        """
        return cast("CustomerAffiliateToStoreResult", self._caller._call("customer.affiliate.toStore", [], {"amount": amount}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class CustomerSubscriptions:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CustomerSubscriptionsListResultItem]:
        """**List subscriptions**

        The buyer's subscriptions at the store, with each one's renewal waiting to be paid, if any. `meta` says what the store lets a buyer do: cancel (and whether at once or when what was paid for runs out), undo a cancellation, pause and for how long, and give another card.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 300 reads in ten minutes.

        Docs: https://docs.shoply.gg/api-reference/customer-api/list-subscriptions
        """
        return cast("List[CustomerSubscriptionsListResultItem]", self._caller._call("customer.subscriptions.list", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def cancel(
        self,
        subscription_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CustomerSubscriptionsCancelResultItem]:
        """**Cancel a subscription**

        As the store's setting says: when what was paid for runs out, or at once. Refused with `cancel_off` where the store does not let buyers cancel. Answers the list again.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 30 changes in ten minutes.

        Docs: https://docs.shoply.gg/api-reference/customer-api/cancel-a-subscription
        """
        return cast("List[CustomerSubscriptionsCancelResultItem]", self._caller._call("customer.subscriptions.cancel", [subscription_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def undo(
        self,
        subscription_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CustomerSubscriptionsUndoResultItem]:
        """**Undo a cancellation**

        Keeps a subscription cancelled for the end of its period renewing, until that period runs out, where the store allows it (`undo_off`). Answers the list again.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 30 changes in ten minutes.

        Docs: https://docs.shoply.gg/api-reference/customer-api/undo-a-cancellation
        """
        return cast("List[CustomerSubscriptionsUndoResultItem]", self._caller._call("customer.subscriptions.undo", [subscription_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def pause(
        self,
        subscription_id: str,
        *,
        days: int,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CustomerSubscriptionsPauseResultItem]:
        """**Pause a subscription**

        Nothing renews until it resumes, and where the store takes access back its keys and files are hidden until then too. It resumes by itself after `days`, or sooner with Resume a subscription. Up to the store's longest pause, as often a year as it allows (`pausesLeft` on each subscription). Refused with `pause_off` where the store does not let buyers pause. Answers the list again.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 30 changes in ten minutes.

        Args:
            days: How long, from 1 to the store's longest pause (`pauseDays` in `meta`). Required.

        Docs: https://docs.shoply.gg/api-reference/customer-api/pause-a-subscription
        """
        return cast("List[CustomerSubscriptionsPauseResultItem]", self._caller._call("customer.subscriptions.pause", [subscription_id], {"days": days}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def resume(
        self,
        subscription_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CustomerSubscriptionsResumeResultItem]:
        """**Resume a subscription**

        Ends a pause the buyer started, now. One the store paused is the store's to end. Answers the list again.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 30 changes in ten minutes.

        Docs: https://docs.shoply.gg/api-reference/customer-api/resume-a-subscription
        """
        return cast("List[CustomerSubscriptionsResumeResultItem]", self._caller._call("customer.subscriptions.resume", [subscription_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def card(
        self,
        subscription_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """**Give another card**

        The address of Stripe's own page where the buyer gives another card for a subscription charged by itself, where the store allows it (`canChangeCard`). Send the buyer there. Once they are done, Stripe sends them back to the store's customer panel, which says whether the card was saved.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 30 changes in ten minutes.

        Docs: https://docs.shoply.gg/api-reference/customer-api/give-another-card
        """
        return cast("Any", self._caller._call("customer.subscriptions.card", [subscription_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class CustomerTickets:

    def __init__(self, caller: Any) -> None:
        self._caller = caller

    def list(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> List[CustomerTicketsListResultItem]:
        """**List support tickets**

        The buyer's support tickets at the store, the latest message first. `status` is `open` (waiting on the store), `answered` or `resolved`. `meta.on` is whether the store takes tickets (off, the list is empty and nothing can be opened), `meta.canOpen` whether the buyer may open one now (one open ticket at a time), `meta.orders` the orders a ticket can be about, each with its `label`, and `meta.limits` what a message may hold.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 300 reads in ten minutes.

        Docs: https://docs.shoply.gg/api-reference/customer-api/list-support-tickets
        """
        return cast("List[CustomerTicketsListResultItem]", self._caller._call("customer.tickets.list", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def create(
        self,
        *,
        subject: str,
        message: str,
        order: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerTicketsCreateResult:
        """**Open a support ticket**

        Opens a ticket with its first message, which the store is told of. One open ticket a buyer at a time (`ticket_open`), 250 open at a store (`store_full`), and 100 messages a day a buyer (`daily_limit`). Refused with `tickets_off` where the store takes none. Pictures are sent from the customer panel. Answers the ticket as Get a support ticket does, and the list in `meta`.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 30 changes in ten minutes.

        Args:
            subject: What it is about, up to 100 characters. Required.
            message: The first message, up to 500 characters. Required.
            order: The order it is about, one of `meta.orders` on List support tickets. Left out, something else.

        Docs: https://docs.shoply.gg/api-reference/customer-api/open-a-support-ticket
        """
        return cast("CustomerTicketsCreateResult", self._caller._call("customer.tickets.create", [], {"subject": subject, "message": message, "order": order}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def show(
        self,
        ticket_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerTicketsShowResult:
        """**Get a support ticket**

        A ticket with its `conversation`, oldest first: each message's `from` (`buyer` or `store`), `body` (Markdown, as written), `html` (the body as Markdown draws it, escaped, which is safe to show as it is), `pictures` and `createdAt`. A picture is named here and shown in the customer panel. `canReopenUntil` is the last moment writing on a resolved ticket opens it again.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 300 reads in ten minutes.

        Docs: https://docs.shoply.gg/api-reference/customer-api/get-a-support-ticket
        """
        return cast("CustomerTicketsShowResult", self._caller._call("customer.tickets.show", [ticket_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def reply(
        self,
        ticket_id: str,
        *,
        message: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerTicketsReplyResult:
        """**Write on a support ticket**

        Writes on the ticket as the buyer, which the store is told of. On a resolved ticket within 30 days it opens it again, if the buyer has no other open ticket; after that, `too_old`. Answers the ticket.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 30 changes in ten minutes.

        Args:
            message: The message, up to 500 characters. Required.

        Docs: https://docs.shoply.gg/api-reference/customer-api/write-on-a-support-ticket
        """
        return cast("CustomerTicketsReplyResult", self._caller._call("customer.tickets.reply", [ticket_id], {"message": message}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def resolve(
        self,
        ticket_id: str,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerTicketsResolveResult:
        """**Resolve a support ticket**

        Marks the buyer's ticket resolved, as their "Mark as Resolved" does. Answers the ticket.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 30 changes in ten minutes.

        Docs: https://docs.shoply.gg/api-reference/customer-api/resolve-a-support-ticket
        """
        return cast("CustomerTicketsResolveResult", self._caller._call("customer.tickets.resolve", [ticket_id], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))


class CustomerResources:
    """The routes, as resources and methods.
    """
    orders: CustomerOrders
    affiliate: CustomerAffiliate
    subscriptions: CustomerSubscriptions
    tickets: CustomerTickets

    def _call(self, id: str, path: List[str], fields: Dict[str, Any], options: Dict[str, Any]) -> Any:
        raise NotImplementedError

    def _resources(self) -> None:
        self.orders = CustomerOrders(self)
        self.affiliate = CustomerAffiliate(self)
        self.subscriptions = CustomerSubscriptions(self)
        self.tickets = CustomerTickets(self)

    def login(
        self,
        *,
        email: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerLoginResult:
        """**Send a sign-in code**

        Emails a six-digit code to the address a buyer typed, for them to type back with Sign in with the code. The code works for 10 minutes, five tries.

        The answer is the same for any address, and a code is only mailed to an address that has orders at the store, so this cannot be used to find out who has bought there. One address is sent a code a minute at most, five an hour and ten a day: past that the answer is `code_cooldown` with `resendIn`, the seconds to wait. A store sends 60 codes an hour at most, and past that, or on a busy hour for the whole platform, the answer is `store_busy`.

        Call it from the buyer's own device. It is counted for the address that asks, 10 an hour, so a server asking for every buyer would run out at once.

        It is counted for the address that asks: 10 an hour.

        Args:
            email: The address the buyer bought with. Required.

        Docs: https://docs.shoply.gg/api-reference/customer-api/send-a-sign-in-code
        """
        return cast("CustomerLoginResult", self._call("customer.login", [], {"email": email}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def verify(
        self,
        *,
        email: str,
        code: str,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerVerifyResult:
        """**Sign in with the code**

        Trades the emailed code for the buyer's token, which every other route of the Customer API takes as `Authorization: Bearer shoply_ct_...`. It reaches this buyer's own orders at this store and nothing else, and works for 30 days.

        Keep it where only your page or app can read it, never in an address. A buyer holds 20 tokens at a store at most: a 21st ends their oldest.

        A wrong code is `code_wrong`, and a code past its 10 minutes or its five tries is `code_expired`. After 20 wrong codes in a day for one address, none is checked for it until the day is over (`code_paused`).

        It is counted for the address that asks: 30 in fifteen minutes.

        Args:
            email: The address the code was sent to. Required.
            code: The six digits from the email. Required.

        Docs: https://docs.shoply.gg/api-reference/customer-api/sign-in-with-the-code
        """
        return cast("CustomerVerifyResult", self._call("customer.verify", [], {"email": email, "code": code}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def show(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerShowResult:
        """**Get the signed-in buyer**

        Everything the customer panel's first page shows: the buyer's email, what they have spent, their store balance, their 200 newest orders, and the downloads, files and setup instructions their paid orders hand over.

        `downloads.files` and `downloads.instructions` are every paid order's together. `downloads.orders` is the same an order at a time, newest first, as the customer panel shows it: each with what it bought, its own files and its own instructions. The store's `buttons` and `general` notes go with every order.

        `affiliate` is null unless the store has an affiliate programme the buyer is in or may join, and `subscriptions` says whether they have ever had one. Keys are not listed here: Get an order has them.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 300 reads in ten minutes.

        Docs: https://docs.shoply.gg/api-reference/customer-api/get-the-signed-in-buyer
        """
        return cast("CustomerShowResult", self._call("customer.show", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def logout(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerLogoutResult:
        """**Sign out**

        Ends the token the request is made with. Their other tokens, and the customer panel, stay signed in.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 30 changes in ten minutes.

        Docs: https://docs.shoply.gg/api-reference/customer-api/sign-out
        """
        return cast("CustomerLogoutResult", self._call("customer.logout", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))

    def logoutEverywhere(
        self,
        *,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> CustomerLogoutEverywhereResult:
        """**Sign out everywhere**

        Ends every token the buyer holds at this store, this one too, and signs them out of its customer panel. `sessions` says how many ended.

        Needs the buyer's token: `Authorization: Bearer shoply_ct_...`, from Sign in with the code.

        It is counted for the buyer's token: 30 changes in ten minutes.

        Docs: https://docs.shoply.gg/api-reference/customer-api/sign-out-everywhere
        """
        return cast("CustomerLogoutEverywhereResult", self._call("customer.logoutEverywhere", [], {}, {"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers}))
