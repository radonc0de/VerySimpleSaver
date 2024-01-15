export default interface Transaction {
	id: number,
	date: number,
	who: string,
	desc: string,
	cat: string,
	amount: number,
	method: number
}