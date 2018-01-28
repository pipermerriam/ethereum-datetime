## Ethereum Date and Time tools

Contract which implements utilities for working with datetime values in
ethereum.

* Contract Address (Main): `0x1a6184CD4C5Bea62B0116de7962EE7315B7bcBce`
* Contract Address (Kovan): `0x71b6e049E78c75fC61480357CD5aA1B81E1b16E0`
* Contract Address (Rinkeby): `0x670b2B167e13b131C491D87bA745dA41f07ecbc3`
* Contract Address (Ropsten): `0x1F0a2ba4B115bd3e4007533C52BBd30C17E8B222`

Compiled with:

```bash
$ solc --version
solc, the solidity compiler commandline interface
Version: 0.1.3-1736fe80/RelWithDebInfo-Darwin/unknown/JIT linked to libethereum-0.9.92-dcf2fd11/RelWithDebInfo-Darwin/unknown/JIT
$ solc contracts/DateTime.sol --optimize --bin
```

To verify, you need to compare the code on the blockchain with the runtime code
which can be gotten from ``solc contracts/DateTime.sol --optimize --bin-runtime``.

Also you can find it already verified at:
* (Main) https://etherscan.io/address/0x1a6184cd4c5bea62b0116de7962ee7315b7bcbce#code
* (Kovan) https://kovan.etherscan.io/address/0x71b6e049e78c75fc61480357cd5aa1b81e1b16e0#code
* (Rinkeby) https://rinkeby.etherscan.io/address/0x670b2b167e13b131c491d87ba745da41f07ecbc3#code
* (Ropsten) https://ropsten.etherscan.io/address/0x1f0a2ba4b115bd3e4007533c52bbd30c17e8b222#code

### DateTime struct

Internally, the following **struct** is used to represent date-time object.

```
struct DateTime {
        uint16 year;
        uint8 month;
        uint8 day;
        uint8 hour;
        uint8 minute;
        uint8 second;
        uint8 weekday;
}
```


### API

* `isLeapYear(uint16 year) constant returns (bool)`

Given an integer year value, returns whether it is a leap year.


* `parseTimestamp(uint timestamp) internal returns (DateTime dt)`

Given a unix timestamp, returns the `DateTime` representation of it.


* `getYear(uint timestamp) constant returns (uint16)`

Given a unix timestamp, returns the `DateTime.year` value for the timestamp.


* `getMonth(uint timestamp) constant returns (uint16)`

Given a unix timestamp, returns the `DateTime.month` value for the timestamp.


* `getDay(uint timestamp) constant returns (uint16)`

Given a unix timestamp, returns the `DateTime.day` value for the timestamp.


* `getHour(uint timestamp) constant returns (uint16)`

Given a unix timestamp, returns the `DateTime.hour` value for the timestamp.


* `getMinute(uint timestamp) constant returns (uint16)`

Given a unix timestamp, returns the `DateTime.minute` value for the timestamp.


* `getSecond(uint timestamp) constant returns (uint16)`

Given a unix timestamp, returns the `DateTime.second` value for the timestamp.


* `getWeekday(uint timestamp) constant returns (uint8)`

Given a unix timestamp, returns the `DateTime.weekday` value for the timestamp.


* `toTimestamp(uint16 year, uint8 month, uint8 day, uint8 hour, uint8 minute, uint8 second) constant returns (uint timestamp)`
* `toTimestamp(uint16 year, uint8 month, uint8 day, uint8 hour, uint8 minute) constant returns (uint timestamp)`
* `toTimestamp(uint16 year, uint8 month, uint8 day, uint8 hour) constant returns (uint timestamp)`
* `toTimestamp(uint16 year, uint8 month, uint8 day) constant returns (uint timestamp)`

Returns the unix timestamp representation for the given date and time values.
