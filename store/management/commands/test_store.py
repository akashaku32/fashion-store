from django.core.management.base import BaseCommand
from store.models import Product, Category, ProductImage


class Command(BaseCommand):
    help = 'Basic testing of the fashion store functionality'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🧪 STARTING STORE TESTING\n'))

        tests_passed = 0
        total_tests = 0

        # Test 1: Database Models
        self.stdout.write('📊 Testing Database Models...')
        try:
            total_tests += 1
            categories = Category.objects.all()
            products = Product.objects.all()
            images = ProductImage.objects.all()

            self.stdout.write('   ✅ Categories: {}'.format(categories.count()))
            self.stdout.write('   ✅ Products: {}'.format(products.count()))
            self.stdout.write('   ✅ Product Images: {}'.format(images.count()))

            # Verify all products have images
            products_without_images = [p.name for p in products if not p.images.exists()]
            if products_without_images:
                self.stdout.write(self.style.ERROR('   ❌ Products without images: {}'.format(products_without_images)))
            else:
                self.stdout.write('   ✅ All products have images')
                tests_passed += 1

        except Exception as e:
            self.stdout.write(self.style.ERROR('   ❌ Database test failed: {}'.format(e)))

        # Test 2: Product Pricing (Rupees)
        self.stdout.write('\n💰 Testing Product Pricing (Rupees)...')
        try:
            total_tests += 1
            all_products = Product.objects.all()

            # Check price format and ranges
            valid_prices = 0
            for product in all_products:
                if product.price > 0 and (product.discount_price is None or product.discount_price <= product.price):
                    valid_prices += 1
                else:
                    self.stdout.write(self.style.WARNING('   ⚠️ Invalid pricing for: {}'.format(product.name)))

            if valid_prices == all_products.count():
                self.stdout.write('   ✅ All {} products have valid pricing'.format(all_products.count()))
                tests_passed += 1
            else:
                self.stdout.write(self.style.WARNING('   ⚠️ {} products have pricing issues'.format(all_products.count() - valid_prices)))

            # Price range analysis
            price_ranges = {
                'Budget (₹0-₹5,000)': len([p for p in all_products if p.final_price <= 5000]),
                'Mid-range (₹5,001-₹15,000)': len([p for p in all_products if 5001 <= p.final_price <= 15000]),
                'Premium (₹15,001-₹50,000)': len([p for p in all_products if 15001 <= p.final_price <= 50000]),
                'Luxury (₹50,001+)': len([p for p in all_products if p.final_price > 50000])
            }

            self.stdout.write('   📊 Price Distribution:')
            for range_name, count in price_ranges.items():
                self.stdout.write('      {}: {} products'.format(range_name, count))

        except Exception as e:
            self.stdout.write(self.style.ERROR('   ❌ Pricing test failed: {}'.format(e)))

        # Test 3: Category Organization
        self.stdout.write('\n📂 Testing Category Organization...')
        try:
            total_tests += 1
            categories = Category.objects.all()

            category_stats = {}
            for category in categories:
                product_count = category.products.count()
                category_stats[category.name] = product_count

            self.stdout.write('   📊 Products per Category:')
            for cat_name, count in category_stats.items():
                self.stdout.write('      {}: {} products'.format(cat_name, count))

            # Check for empty categories
            empty_categories = [cat.name for cat in categories if cat.products.count() == 0]
            if empty_categories:
                self.stdout.write(self.style.WARNING('   ⚠️ Empty categories: {}'.format(empty_categories)))
            else:
                self.stdout.write('   ✅ No empty categories')
                tests_passed += 1

        except Exception as e:
            self.stdout.write(self.style.ERROR('   ❌ Category test failed: {}'.format(e)))

        # Test 4: Featured Products
        self.stdout.write('\n⭐ Testing Featured Products...')
        try:
            total_tests += 1
            featured_products = Product.objects.filter(is_featured=True)
            self.stdout.write('   📊 Featured Products: {}'.format(featured_products.count()))

            if featured_products.count() > 0:
                self.stdout.write('   ✅ Featured products exist')
                tests_passed += 1
            else:
                self.stdout.write(self.style.WARNING('   ⚠️ No featured products found'))

        except Exception as e:
            self.stdout.write(self.style.ERROR('   ❌ Featured products test failed: {}'.format(e)))

        # Final Test Summary
        self.stdout.write('\n' + '='*60)
        self.stdout.write(self.style.SUCCESS('🎉 TESTING COMPLETE'))
        self.stdout.write('='*60)

        success_rate = (tests_passed * 100.0) / total_tests if total_tests > 0 else 0

        if success_rate >= 90:
            self.stdout.write(self.style.SUCCESS('✅ EXCELLENT: {}/{} tests passed ({:.1f}%)'.format(tests_passed, total_tests, success_rate)))
            self.stdout.write(self.style.SUCCESS('🎊 Your fashion store is ready for deployment!'))
        elif success_rate >= 75:
            self.stdout.write(self.style.WARNING('⚠️ GOOD: {}/{} tests passed ({:.1f}%)'.format(tests_passed, total_tests, success_rate)))
            self.stdout.write('Some minor issues to address.')
        else:
            self.stdout.write(self.style.ERROR('❌ NEEDS ATTENTION: {}/{} tests passed ({:.1f}%)'.format(tests_passed, total_tests, success_rate)))
            self.stdout.write('Several issues need to be fixed.')

        # Quick stats summary
        self.stdout.write('\n📊 STORE SUMMARY:')
        self.stdout.write('   🏪 Categories: {}'.format(Category.objects.count()))
        self.stdout.write('   👗 Products: {}'.format(Product.objects.count()))
        self.stdout.write('   🖼️ Product Images: {}'.format(ProductImage.objects.count()))
        self.stdout.write('   ⭐ Featured Products: {}'.format(Product.objects.filter(is_featured=True).count()))
        self.stdout.write('   📦 In Stock: {}'.format(Product.objects.filter(stock_quantity__gt=0).count()))

        # Price range summary
        products = Product.objects.all()
        price_ranges = {
            'Budget (₹0-₹5,000)': len([p for p in products if p.final_price <= 5000]),
            'Mid-range (₹5,001-₹15,000)': len([p for p in products if 5001 <= p.final_price <= 15000]),
            'Premium (₹15,001-₹50,000)': len([p for p in products if 15001 <= p.final_price <= 50000]),
            'Luxury (₹50,001+)': len([p for p in products if p.final_price > 50000])
        }

        self.stdout.write('\n💰 PRICE DISTRIBUTION:')
        for range_name, count in price_ranges.items():
            if count > 0:
                self.stdout.write('   {}: {} products'.format(range_name, count))

        self.stdout.write('\n🌟 READY FOR DEMONSTRATION!' if success_rate >= 90 else '\n⚠️ SOME ISSUES TO ADDRESS')
