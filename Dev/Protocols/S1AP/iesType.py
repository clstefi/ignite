#
# Copyright (c) 2019, Infosys Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

IES_TYPE = {
        "0" : "MME-UE-S1AP-ID",
        "1" : "HandoverType",
        "2" : "Cause",
        "3" : "SourceID",
        "4" : "TargetID",
        "8" : "ENB-UE-S1AP-ID",
        "12" : "E-RABSubjecttoDataForwardinglist",
        "13" : "E-RABtoReleaselistHOCmd",
        "14" : "E-RABDataForwardingItem",
        "15" : "E-RABReleaseItemBearerRelComp",
        "16" : "E-RABToBeSetuplistBearerSUReq",
        "17" : "E-RABToBeSetupItemBearerSUReq",
        "18" : "E-RABAdmittedlist",
        "19" : "E-RABFailedToSetuplistHOReqAck",
        "20" : "E-RABAdmittedItem",
        "21" : "E-RABFailedtoSetupItemHOReqAck",
        "22" : "E-RABToBeSwitchedDLlist",
        "23" : "E-RABToBeSwitchedDLItem",
        "24" : "E-RABToBeSetupListCtxtSUReq",
        "25" : "TraceActivation",
        "26" : "NAS-PDU",
        "27" : "E-RABToBeSetupItemHOReq",
        "28" : "E-RABSetuplistBearerSURes",
        "29" : "E-RABFailedToSetuplistBearerSURes",
        "30" : "E-RABToBeModifiedlistBearerModReq",
        "31" : "E-RABModifylistBearerModRes",
        "32" : "E-RABFailedToModifylist",
        "33" : "E-RABToBeReleasedlist",
        "34" : "E-RABFailedToReleaselist",
        "35" : "E-RABItem",
        "36" : "E-RABToBeModifiedItemBearerModReq",
        "37" : "E-RABModifyItemBearerModRes",
        "38" : "E-RABReleaseItem",
        "39" : "E-RABSetupItemBearerSURes",
        "40" : "SecurityContext",
        "41" : "HandoverRestrictionlist",
        "43" : "UEPagingID",
        "44" : "PagingDRX",
        "46" : "TAIList",
        "47" : "TAIItem",
        "48" : "E-RABFailedToSetuplistCtxtSURes",
        "49" : "E-RABReleaseItemHOCmd",
        "50" : "E-RABSetupItemCtxtSURes",
        "51" : "E-RABSetupListCtxtSURes",
        "52" : "E-RABToBeSetupItemCtxtSUReq",
        "53" : "E-RABToBeSetuplistHOReq",
        "55" : "GERANtoLTEHOInformationRes",
        "57" : "UTRANtoLTEHOInformationRes",
        "58" : "CriticalityDiagnostics",
        "59" : "Global-ENB-ID",
        "60" : "ENBname",
        "61" : "MMEname",
        "63" : "ServedPLMNs",
        "64" : "SupportedTAs",
        "65" : "TimeToWait",
        "66" : "UEAggregateMaximumBitrate",
        "67" : "TAI",
        "69" : "E-RABReleaselistBearerRelComp",
        "70" : "Cdma2000PDU",
        "71" : "Cdma2000RATType",
        "72" : "Cdma2000SectorID",
        "73" : "SecurityKey",
        "74" : "UERadioCapability",
        "75" : "GUMMEI-ID",
        "78" : "E-RABInformationlistItem",
        "79" : "Direct-Forwarding-Path-Availability",
        "80" : "UEIdentityIndexValue",
        "83" : "Cdma2000HOStatus",
        "84" : "Cdma2000HORequiredIndication",
        "86" : "E-UTRAN-Trace-ID",
        "87" : "RelativeMMECapacity",
        "88" : "SourceMME-UE-S1AP-ID",
        "89" : "Bearers-SubjectToStatusTransfer-Item",
        "90" : "ENB-StatusTransfer-TransparentContainer",
        "91" : "UE-associatedLogicalS1-ConnectionItem",
        "92" : "ResetType",
        "93" : "UE-associatedLogicalS1-ConnectionlistResAck",
        "94" : "E-RABToBeSwitchedULItem",
        "95" : "E-RABToBeSwitchedULlist",
        "96" : "S-TMSI",
        "97" : "Cdma2000OneXRAND",
        "98" : "RequestType",
        "99" : "UE-S1AP-IDs",
        "100" : "EUTRAN-CGI",
        "101" : "OverloadResponse",
        "102" : "Cdma2000OneXSRVCCInfo",
        "103" : "E-RABFailedToBeReleasedlist",
        "104" : "Source-ToTarget-TransparentContainer",
        "105" : "ServedGUMMEIs",
        "106" : "SubscriberProfileIDforRFP",
        "107" : "UESecurityCapabilities",
        "108" : "CSFallbackIndicator",
        "109" : "CNDomain",
        "110" : "E-RABReleasedlist",
        "111" : "MessageIdentifier",
        "112" : "SerialNumber",
        "113" : "WarningArealist",
        "114" : "RepetitionPeriod",
        "115" : "NumberofBroadcastRequest",
        "116" : "WarningType",
        "117" : "WarningSecurityInfo",
        "118" : "DataCodingScheme",
        "119" : "WarningMessageContents",
        "120" : "BroadcastCompletedArealist",
        "121" : "Inter-SystemInformationTransferTypeEDT",
        "122" : "Inter-SystemInformationTransferTypeMDT",
        "123" : "Target-ToSource-TransparentContainer",
        "124" : "SRVCCOperationPossible",
        "125" : "SRVCCHOIndication",
        "126" : "NAS-DownlinkCount",
        "127" : "CSG-Id",
        "128" : "CSG-Idlist",
        "129" : "SONConfigurationTransferECT",
        "130" : "SONConfigurationTransferMCT",
        "131" : "TraceCollectionEntityIPAddress",
        "132" : "MSClassmark2",
        "133" : "MSClassmark3",
        "134" : "RRC-Establishment-Cause",
        "135" : "NASSecurityParametersfromE-UTRAN",
        "136" : "NASSecurityParameterstoE-UTRAN",
        "137" : "PagingDRX",
        "138" : "Source-ToTarget-TransparentContainer-Secondary",
        "139" : "Target-ToSource-TransparentContainer-Secondary",
        "140" : "EUTRANRoundTripDelayEstimationInfo",
        "141" : "BroadcastCancelledArealist",
        "142" : "ConcurrentWarningMessageIndicator",
        "143" : "Data-Forwarding-Not-Possible",
        "144" : "ExtendedRepetitionPeriod",
        "145" : "CellAccessMode",
        "146" : "CSGMembershipStatus",
        "147" : "LPPa-PDU",
        "148" : "Routing-ID",
        "149" : "Time-Synchronisation-Info",
        "150" : "PS-ServiceNotAvailable",
        "151" : "PagingPriority",
        "152" : "X2TNLConfigurationInfo",
        "153" : "ENBX2ExtendedTransportLayerAddresses",
        "154" : "GUMMEIlist",
        "155" : "GW-TransportLayerAddress",
        "156" : "Correlation-ID",
        "157" : "SourceMME-GUMMEI",
        "158" : "MME-UE-S1AP-ID-2",
        "159" : "RegisteredLAI",
        "160" : "RelayNode-Indicator",
        "161" : "TrafficLoadReductionIndication",
        "162" : "MDTConfiguration",
        "163" : "MMERelaySupportIndicator",
        "164" : "GWContextReleaseIndication",
        "165" : "ManagementBasedMDTAllowed",
        "166" : "PrivacyIndicator",
        "167" : "Time-UE-StayedInCell-EnhancedGranularity",
        "168" : "HO-Cause",
        "169" : "VoiceSupportMatchIndicator",
        "170" : "GUMMEIType",
        "171" : "M3Configuration",
        "172" : "M4Configuration",
        "173" : "M5Configuration",
        "174" : "MDT-Location-Info",
        "175" : "MobilityInformation",
        "176" : "Tunnel-Information-for-BBF",
        "177" : "ManagementBasedMDTPLMNlist",
        "178" : "SignallingBasedMDTPLMNlist",
        "179" : "ULCOUNTValueExtended",
        "180" : "DLCOUNTValueExtended",
        "181" : "ReceiveStatusOfULPDCPSDUsExtended",
        "182" : "ECGIlistForRestart",
        "183" : "SIPTO-Correlation-ID",
        "184" : "SIPTO-L-GW-TransportLayerAddress",
        "185" : "TransportInformation",
        "186" : "LHN-ID",
        "187" : "AdditionalCSFallbackIndicator",
        "188" : "TAIlistForRestart",
        "189" : "UserLocationInformation",
        "190" : "EmergencyAreaIDlistForRestart",
        "191" : "KillAllWarningMessages",
        "192" : "Masked-IMEISV",
        "193" : "ENBIndirectX2TransportLayerAddresses",
        "194" : "UE-HistoryInformationFromTheUE",
        "195" : "ProSeAuthorized",
        "196" : "ExpectedUEBehaviour",
        "197" : "LoggedMBSFNMDT",
        "198" : "UERadioCapabilityForPaging",
        "199" : "E-RABToBeModifiedlistBearerModInd",
        "200" : "E-RABToBeModifiedItemBearerModInd",
        "201" : "E-RABNotToBeModifiedlistBearerModInd",
        "202" : "E-RABNotToBeModifiedItemBearerModInd",
        "203" : "E-RABModifylistBearerModConf",
        "204" : "E-RABModifyItemBearerModConf",
        "205" : "E-RABFailedToModifylistBearerModConf",
        "206" : "SON-Information-Report",
        "207" : "Muting-Availability-Indication",
        "208" : "Muting-Pattern-Information",
        "209" : "Synchronisation-Information",
        "210" : "E-RABToBeReleasedlistBearerModConf",
        "211" : "AssistanceDataForPaging",
        "212" : "CellIdentifierAndCELevelForCECapableUEs",
        "213" : "InformationOnRecommendedCellsAndENBsForPaging",
        "214" : "RecommendedCellItem",
        "215" : "RecommendedENBItem",
        "216" : "ProSeUEtoNetworkRelaying",
        "217" : "ULCOUNTValuePDCP-SNlength18",
        "218" : "DLCOUNTValuePDCP-SNlength18",
        "219" : "ReceiveStatusOfULPDCPSDUsPDCP-SNlength18",
        "220" : "M6Configuration",
        "221" : "M7Configuration",
        "222" : "PWSfailedECGIlist",
        "223" : "MME-Group-ID",
        "224" : "Additional-GUTI",
        "225" : "S1-Message",
        "226" : "CSGMembershipInfo",
        "227" : "Paging-eDRXInformation",
        "228" : "UE-RetentionInformation",
        "230" : "UE-Usage-Type",
        "231" : "Extended-UEIdentityIndexValue"}