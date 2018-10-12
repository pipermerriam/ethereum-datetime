## Ethereum Date and Time tools

Contract which implements utilities for working with datetime values in
ethereum.

Contract Deployments: 

- Mainnet: [`0x1a6184CD4C5Bea62B0116de7962EE7315B7bcBce`](https://etherscan.io/address/0x1a6184cd4c5bea62b0116de7962ee7315b7bcbce)
- Rinkeby: [`0x92482Ba45A4D2186DafB486b322C6d0B88410FE7`](https://rinkeby.etherscan.io/address/0x92482ba45a4d2186dafb486b322c6d0b88410fe7)


To verify, you need to compare the code on the blockchain with the runtime code
which can be gotten from ``solc contracts/DateTime.sol --optimize --bin-runtime``.

Also you can find it already verified at https://etherscan.io/address/0x1a6184cd4c5bea62b0116de7962ee7315b7bcbce#code

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
